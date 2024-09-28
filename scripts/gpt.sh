#!/usr/bin/env python
import os
import requests
import base64
import glob
import json
from datetime import datetime

# Configuration
API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("AZURE_OPENAI_API_KEY environment variable is not set")

ENDPOINT = "https://samj-oai-westus.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"

headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def process_townhall(transcript_path, presentation_path, previous_analyses):
    transcript = read_file(transcript_path)
    presentation = read_file(presentation_path)
    
    # Extract date and townhall number from filename
    filename = os.path.basename(transcript_path)
    date_str = filename[:10]
    townhall_number = filename.split('_')[2].split('.')[0]
    
    # Format date if it's a valid date string, otherwise use original string
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%B %d, %Y")
    except ValueError:
        date = date_str

    system_prompt = """You are an AI assistant reviewing Open Source Initiative townhalls on Open Source AI to analyze the process and outcomes.
    Focus on the inclusion or exclusion of training data in OSAID requirements and its impact on the four essential freedoms."""

    user_prompt = f"""Analyze the following townhall materials for OSI Townhall {townhall_number} held on {date}. 
    Pay attention to discussions about including or excluding training data, and any potential process problems, biases, etc.
    Surface any potential predetermined positions, decisions, or foregone conclusions relating to data, especially in the first few townhalls.

    Presentation:
    {presentation}

    Transcript:
    {transcript}

    Previous Townhall Analyses:
    {previous_analyses}

    Consider the previous analyses for context and continuity. Highlight any changes, developments, or contradictions in positions or discussions compared to previous townhalls.

    Provide an analysis in the specified JSON format."""

    json_schema = {
        "type": "object",
        "properties": {
            "townHallNumber": {
                "type": "string",
                "description": "Town Hall number"
            },
            "date": {
                "type": "string",
                "description": "Date of the Town Hall"
            },
            "overview": {
                "type": "string",
                "description": "Brief description of the meeting and any noteworthy details (e.g. breakthroughs, challenges, conflicts, atmosphere, etc.)"
            },
            "keyTakeaways": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "List of key takeaways from the meeting"
            },
            "dataMentions": {
                "type": "string",
                "description": "Any mentions of including, excluding, or substituting data"
            },
            "quotes": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "Verbatim key quotes from the transcript, without attribution to specific speakers"
            }
        },
        "required": ["townHallNumber", "date", "overview", "keyTakeaways", "dataMentions", "quotes"]
    }

    payload = {
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 16384,
        "response_format": {"type": "json_object"},
        "function_call": {"name": "analyze_townhall"},
        "functions": [
            {
                "name": "analyze_townhall",
                "description": "Analyze the townhall and return structured data",
                "parameters": json_schema
            }
        ]
    }

    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()['choices'][0]['message']['function_call']['arguments']
        return json.loads(result)
    except requests.RequestException as e:
        print(f"Failed to process townhall {townhall_number}. Error: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response content: {e.response.text}")
        return None

def main():
    # Sort townhalls by number (assuming format "YYYY-MM-DD_TownHall_XX.srt")
    townhalls = sorted(glob.glob('townhalls/*.srt'), 
                       key=lambda x: int(os.path.basename(x).split('_')[2].split('.')[0]))
    previous_analyses = []

    for transcript_path in townhalls:
        presentation_path = f"presentations/{os.path.basename(transcript_path).replace('.srt', '.txt')}"
        
        if not os.path.exists(presentation_path):
            print(f"Presentation file not found for {transcript_path}")
            continue
        
        # Join previous analyses into a single string, with clear demarcation
        previous_analyses_str = "\n\n".join([
            f"--- Analysis for Townhall {analysis['townHallNumber']} ---\n{json.dumps(analysis, indent=2)}"
            for analysis in previous_analyses
        ])
        
        result = process_townhall(transcript_path, presentation_path, previous_analyses_str)
        if result:
            base_name = os.path.basename(transcript_path).replace('.srt', '')
            
            # Save JSON output
            json_path = f"analysis/{base_name}_analysis.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            print(f"JSON analysis saved to {json_path}")
            
            # Save Markdown output
            md_path = f"analysis/{base_name}_analysis.md"
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(f"# Town Hall {result['townHallNumber']} - {result['date']}\n\n")
                f.write(f"## Overview:\n{result['overview']}\n\n")
                f.write("## Key Takeaways\n")
                for takeaway in result['keyTakeaways']:
                    f.write(f"- {takeaway}\n")
                f.write(f"\n## Data Mentions\n{result['dataMentions']}\n\n")
                f.write("## Quotes\n")
                for i, quote in enumerate(result['quotes'], 1):
                    f.write(f"{i}. \"{quote}\"\n")
                f.write("\n")
            print(f"Markdown analysis saved to {md_path}")
            
            # Add the current analysis to the list of previous analyses
            previous_analyses.append(result)

if __name__ == "__main__":
    main()
