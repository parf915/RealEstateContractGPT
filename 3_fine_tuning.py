import openai
# Redundant import; "from openai import OpenAI" is unnecessary when "import openai" is already used.
# from openai import OpenAI

# Function to read content from a file
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# Function to append content to a file
def save_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        outfile.write(content)

# API key for OpenAI; should ideally be managed through environment variables for security
api_key = 'sk-.......'
client = openai.OpenAI(api_key=api_key)

# ID of the training file previously uploaded to OpenAI
training_file_id = 'file-.....'
# Name of the model to be fine-tuned
model_name = 'gpt-3.5-turbo-1106'

# Creating a fine-tuning job with the specified training file and model
response = client.fine_tuning.jobs.create(
    training_file=training_file_id, model=model_name)

# The job ID is directly assigned to the entire response.

job_id = response['id']

print(f"Fine tuning job created successfully with ID:{job_id}")
