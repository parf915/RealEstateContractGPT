# Real Estate Contract Analysis with GPT-3

## Overview

This repository hosts Python scripts for analyzing real estate purchase agreements with OpenAI's GPT-3, designed to extract crucial information such as names, identification numbers, roles in the contract, amounts, and currencies involved. Given the sensitivity of personal data, the project employs fictitious examples for fine-tuning the model, though it has analyzed over 100,000 real purchase and sale contracts from the past five years.

## Contents

- `pdf_to_txt.py`: Converts PDF documents into text files for analysis.
- `prepare_fine_tuning.py`: Prepares and uploads data for fine-tuning the GPT-3 model.
- `fine_tuning.py`: Initiates the fine-tuning process with OpenAI.
- `model_pdf_gpt.py`: Analyzes contract text to extract structured information.

## Usage

1. Install dependencies: `pip install -r requirements.txt`.
2. Place contract PDFs in the specified directory.
3. Run scripts in the sequence listed.
4. Review extracted information in the generated CSV file.

## JSONL for Fine-Tuning

The `.JSONL` file needed for fine-tuning the model with fictitious data examples is included, reflecting the analysis approach for over 100,000 real contracts over the last five years, respecting data privacy concerns.

## Security Note

API keys and sensitive data are handled securely, assuming responsible data management practices.

## Disclaimer

This tool is for research and informational purposes, ensuring data handling complies with privacy laws and regulations.
