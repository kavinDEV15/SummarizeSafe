from fastapi import FastAPI, Request
import pandas as pd
from utils import extract_text_and_summary
import requests
import json

app = FastAPI()

# Load the dataset
df = pd.read_csv('./data/dataset.csv')

@app.get("/extract/")
def extract(convo_id: str):
    """
    Extract the text and summary for a given conversation ID.
    """
    text, summary = extract_text_and_summary(df, convo_id)
    return {"text": text, "summary": summary}

@app.post("/check_hallucinations/")
async def check_hallucinations(request: Request):
    """
    Check for hallucinations in the summary of a given conversation ID.
    """
    
    req_body = await request.json()
    convo_id = req_body.get("convo_id")
    
    
    text, summary = extract_text_and_summary(df, convo_id)

   
    if not text or not summary:
        return {"error": "Text or summary not found for the given conversation ID."}

    # Prompt for the LLM
    prompt = f"""
You are an expert hallucinations detector. Your task is to carefully analyze the relationship between the given conversation text and its associated summary.

### Text:
{text}

### Summary:
{summary}

### Task:
1. Verify whether the summary accurately represents the key points of the text. 
2. Identify any parts of the summary that include information not supported by the text, such as fabricated details or hallucinated content.
3. If any fabricated or hallucinated information is found, list the specific phrases or sentences from the summary and explain why they are not consistent with the text.
4. If the summary is accurate, state "The summary accurately reflects the text without any hallucinations."

### Response format:
- Conclusion: [Is the summary accurate or contains hallucinated content?]
- Hallucinated parts (if any): [List of hallucinated parts with reasons]
- Overall analysis: [Short analysis of the relationship between text and summary]

Be as concise and clear as possible in your analysis.
"""

    try:
        # Send request to the locally running Ollama model
        response = requests.post(
            "http://localhost:11434/api/generate", 
            json={"model": "llama3", "prompt": prompt}
        )
        response.raise_for_status()

        # Collect the streaming responses into a single paragraph
        combined_response = ""
        for line in response.text.splitlines():
            try:
                # Parse each JSON response
                llm_chunk = json.loads(line)
                combined_response += llm_chunk.get('response', '')
            except json.JSONDecodeError:
                
                continue

        # Log the combined response for debugging
        print(f"Combined Response: {combined_response}")

        # Check if any hallucinations are found in the combined response
        hallucination_count = 1 if "fabricated" in combined_response or "hallucinated" in combined_response else 0
        conclusion = "Hallucinations present" if hallucination_count > 0 else "No hallucinations"

        return {
            "text": text,
            "summary": summary,
            "hallucinations": combined_response.strip(),  
            "hallucination_count": hallucination_count,
            "conclusion": conclusion
        }
    except requests.exceptions.RequestException as e:
        # Log the error message
        print(f"Error: {str(e)}")
        return {"error": str(e), "message": "Error communicating with the local Ollama model."}
