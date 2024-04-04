import openai
# The OpenAI import is duplicated; only one import statement is needed.
from openai import OpenAI

# Function to open a file and return its contents
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# Function to append content to a file
def save_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        outfile.write(content)

# OpenAI API key; it's better to use environment variables for security
api_key = 'sk-..........'		
client = OpenAI(api_key=api_key)

# Path to the JSONL file containing training data
training_data_path = '/Users/renzo/Downloads/json_divorcios_2.jsonl'

# Opening the training data file and uploading it to OpenAI for fine-tuning
with open(training_data_path, "rb") as file:
    response = client.files.create(file=file, purpose="fine-tune")

# Extracting the file ID from the response. 
# The commented-out line correctly shows how to extract the ID, but it's overwritten by the entire response.
# It's important to uncomment and use the correct line for specific operations requiring the file ID.
# file_id = response['id']
file_id = response
print(f"file uploaded successfully with ID:{file_id}")

# Examples of file IDs, possibly from previous uploads. These are commented out but can serve as references.
# file-.....
# file-.....
