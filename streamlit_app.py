import streamlit as st
import requests

# Initialize session state for storing conversation data
if 'text' not in st.session_state:
    st.session_state['text'] = ""
if 'summary' not in st.session_state:
    st.session_state['summary'] = ""
if 'hallucination_result' not in st.session_state:
    st.session_state['hallucination_result'] = None

st.title("Hallucination Detection System")

# User inputs conversation ID
convo_id = st.text_input("Enter Conversation ID:")

if st.button("Fetch Conversation"):
    try:
        # Fetch text and summary from FastAPI backend
        response = requests.get(f"http://localhost:8000/extract/?convo_id={convo_id}")
        data = response.json()

        # Store fetched text and summary in session state
        st.session_state['text'] = data.get("text", "")
        st.session_state['summary'] = data.get("summary", "")

        # Clear previous hallucination results
        st.session_state['hallucination_result'] = None

    except Exception as e:
        st.error(f"Error: {str(e)}")

# Display the extracted text and summary if fetched
if st.session_state['text'] and st.session_state['summary']:
    st.subheader("Extracted Text")
    st.write(st.session_state['text'])

    st.subheader("Summary")
    st.write(st.session_state['summary'])

    # Button to detect hallucinations after fetching conversation
    if st.button("Detect Hallucinations"):
        try:
            # Trigger hallucination detection using POST request with JSON body
            hallucination_response = requests.post(
                "http://localhost:8000/check_hallucinations/",
                json={"convo_id": convo_id}  # Send convo_id in the request body
            )
            
            # Log the response for debugging
            # st.write(f"Response status: {hallucination_response.status_code}")
            # st.write(f"Response text: {hallucination_response.text}")

            # Parse the response
            hallucination_data = hallucination_response.json()

            # Store the hallucination result in session state
            st.session_state['hallucination_result'] = hallucination_data

        except Exception as e:
            st.error(f"Error: {str(e)}")

# Display hallucination detection result if available
if st.session_state['hallucination_result']:
    st.subheader("Hallucination Detection Result")
    result = st.session_state['hallucination_result']
    st.write(result.get("conclusion", "No result"))

    if result.get("hallucination_count", 0) > 0:
        st.write("Hallucinated Parts:", result.get("hallucinations", ""))