from transformers import pipeline

# Load a pre-trained summarization model
summarizer = pipeline("summarization")

def summarize_text(text):
    # Summarize the provided text
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']
