# promptgen

README for Survey Analysis Tool
Overview
This Survey Analysis Tool is designed to automate the categorization of survey responses using OpenAI's language models. It reads survey questions from a CSV file, generates prompts based on these questions, and uses OpenAI's API to categorize the responses into distinct groups. The categorized responses are then saved to a new CSV file for further analysis.

Requirements
Python 3.x
pandas (Python library)
openai (Python library)
Installation
Before running the script, ensure that you have Python installed on your machine. Then, install the required packages using pip:

Setup
API Key: You need an API key from OpenAI. Set this key as an environment variable named OPENAI_API_KEY. This can be done in Unix-based systems with the command:

Data File: Prepare your CSV file with survey questions. The CSV should have at least one column named 'Question' containing the survey questions.

Usage
Running the Script: Run the script with your Python interpreter. Ensure that the path to your CSV file is correctly specified in the script.

Output: The script will output a file named categorized_responses.csv, containing the original survey questions and their categorized responses.

Code Structure
Import necessary libraries.
Set the OpenAI API key from an environment variable for security.
Define functions for creating prompts and getting categories from OpenAI.
Load the survey questions from a CSV file.
Process each question to generate categories.
Save the results to a new CSV file.
Error Handling
The script includes basic error handling for API interactions. Ensure that your internet connection is stable and the API key is correctly set before running the script.

Security and Data Privacy
The script uses environment variables to handle API keys, which is a secure practice.
Ensure that the input and output data do not contain sensitive or personally identifiable information unless it's necessary and handled appropriately.
Contribution

Feel free to fork this repository and contribute to the development. For any major changes, please open an issue first to discuss what you would like to change.

