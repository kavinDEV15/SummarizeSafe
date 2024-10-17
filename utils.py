import pandas as pd

def extract_text_and_summary(df, convo_id):
    """
    Extracts conversation text (as a single paragraph) and the associated summary for a given conversation ID.
    """
    # Filter the rows for the given conversation ID
    convo_data = df[df['Column1'] == convo_id]

    # Concatenate text for this conversation ID
    text = " ".join(convo_data['Column5'].dropna().tolist())

    # Extract the summary (it's only available in the first row of each conversation)
    summary = convo_data['Column6'].dropna().iloc[0] if not convo_data['Column6'].dropna().empty else ""

    return text, summary
