import pandas as pd
import openai

# Anonymized and safe way to handle API keys
# Ensure you have set OPENAI_API_KEY in your environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to create prompt
def create_prompt(question):
    return (
        'You are an expert survey analyst. Your task is to write bespoke prompts for an LLM survey analysis tool based on the survey question being asked.'
        f'Read the survey question: "{question}". Based on this survey question, print out a bespoke prompt relevant to the survey question.'
        'It should follow the template: '
        '"Based on these responses, categorize them into a maximum of 25 distinct categories that reflect (your insertion here). Focus on creating '
        'categories that represent (your insertion here), Use Not applicable for responses that arent relevant or dont answer the question."'
        'For example, for the question "How did you first hear about us?" you would return: '
        'Based on these responses, categorize them into a maximum of 25 distinct categories that reflect different sources of awareness. Focus on creating '
        'categories that represent various channels or methods through which respondents might have heard about us, such as online, social media, word of mouth, '
        'advertisement, television, etc. Use Not applicable for responses that arent relevant or dont answer the question.'
    )

# Function to get categories from OpenAI
def get_categories(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("An error occurred:", e)
        return ""

# Load your CSV file
# Ensure the file path is generic or passed as an argument
df = pd.read_csv('path/to/your/ChatGPTprompts.csv')

# Print the column names to verify
print("Column names in the CSV file:", df.columns.tolist())

# Prepare a list to store results
results = []

# Process each row in the dataframe
for index, row in df.iterrows():
    prompt = create_prompt(row['Question'])
    categories = get_categories(prompt)
    results.append({'Question': row['Question'], 'Categories': categories})

# Convert results to a DataFrame and save to a new CSV file
results_df = pd.DataFrame(results)
results_df.to_csv('categorized_responses.csv', index=False)

# This will create a file named 'categorized_responses.csv' with the results.
