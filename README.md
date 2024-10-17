

```markdown
# SummarizeSafe: Hallucination Detection System

## Overview

**SummarizeSafe** is a state-of-the-art hallucination detection system designed to analyze the accuracy of text summaries using **Ollama's LLM** and machine learning techniques. The system provides a streamlined user interface through **Streamlit**, and processes data using a robust **FastAPI** backend, ensuring that users can easily detect and understand hallucinated or fabricated content in their summaries.

### Key Features:
- **User-friendly Interface**: Powered by **Streamlit**, the front-end allows users to interact with the system by providing conversation IDs.
- **Backend Efficiency**: Built on **FastAPI**, the backend efficiently handles the extraction of conversation data from a dataset, processes it, and communicates with **Ollama LLM** for analysis.
- **Accurate Hallucination Detection**: The system uses cutting-edge large language models (LLMs) from **Ollama** to identify fabricated or hallucinated content in summaries, ensuring the highest degree of accuracy.

---

## Project Setup

### Prerequisites

To get started with **SummarizeSafe**, ensure you have the following installed:

- **Python 3.8+**
- **pip** (Python package manager)
- **Virtual Environment** setup (recommended)
- **Ollama LLM** running locally

### Steps to Install

1. **Clone the Repository**

   ```bash
   git clone https://github.com/kavinDEV15/SummarizeSafe.git
   cd SummarizeSafe
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to isolate dependencies:
   
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Linux/MacOS
   env\Scripts\activate  # For Windows
   ```

3. **Install Required Dependencies**

   After setting up your environment, install the necessary packages by running:
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Ollama Locally**

   Make sure Ollama LLM is running locally:
   
   ```bash
   ollama serve --model llama3
   ```

---

## Running the Project

To start using **SummarizeSafe**, follow these steps:

### 1. **Start the FastAPI Backend**

   Start the backend server with FastAPI:
   
   ```bash
   uvicorn main:app --reload
   ```

   The server will be running at `http://localhost:8000`.

### 2. **Start the Streamlit Frontend**

   Start the **Streamlit** app to interact with the hallucination detection system:
   
   ```bash
   streamlit run streamlit_app.py
   ```

   The frontend will be available at `http://localhost:8501`.

### 3. **Using the System**

   1. Enter a **Conversation ID** in the provided input box.
   2. Click **Fetch Conversation** to retrieve the conversation text and summary.
   3. Click **Detect Hallucinations** to analyze the summary for any fabricated or hallucinated content.
   4. View the results, which will display any hallucinated parts along with a conclusion.

---

## System Components

### 1. **Streamlit Frontend**

The **Streamlit** interface is a web-based frontend that allows users to interact with the system by providing conversation IDs. The frontend sends the provided ID to the FastAPI backend, which fetches the relevant text and summary, and then runs hallucination detection using the Ollama LLM.

### 2. **FastAPI Backend**

The **FastAPI** backend handles the core logic:
- Fetches conversation text and summaries from a dataset.
- Sends prompts to the Ollama LLM model for analysis.
- Returns the results to the frontend.

### 3. **Ollama LLM**

The **Ollama LLM** performs the critical task of analyzing the relationship between conversation text and its summary, detecting any hallucinated content. It takes the text and summary as inputs, analyzes the consistency, and returns the result, which is displayed by the frontend.

### 4. **Dataset (CSV)**

The dataset is stored in a CSV file and contains conversation IDs, texts, and summaries. The backend uses this dataset to retrieve the appropriate data based on the user's input.

---

## Project Structure

```
SummarizeSafe/
│
├── data/                   # Contains the dataset (CSV) for conversations
├── env/                    # Virtual environment (ignored in .gitignore)
├── main.py                 # FastAPI backend logic
├── requirements.txt        # List of required dependencies
├── streamlit_app.py        # Streamlit frontend logic
├── utils.py                # Utility functions for handling dataset extraction
├── .gitignore              # Git ignore file for ignoring virtual environments and cache
```

---

## Sample Prompt for Ollama LLM

We utilize an optimized prompt for the LLM to ensure accurate results:

```python
prompt = f"""
You are an expert summarization auditor. Your task is to carefully analyze the relationship between the given conversation text and its associated summary.

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
```

---

## Future Improvements

- **Automated Dataset Updates**: Automatically update the dataset with new conversation data.
- **Advanced NLP Techniques**: Enhance hallucination detection using advanced NLP techniques beyond large language models.
- **Cloud Deployment**: Deploy the system to a cloud provider (e.g., AWS, Heroku) for wider accessibility.

---

## Contributions

We welcome contributions to **SummarizeSafe**! If you want to contribute, please:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request, and include clear descriptions of your changes.

---


Now, you can copy and paste the above markdown directly into your `README.md` file. Let me know if it works!
