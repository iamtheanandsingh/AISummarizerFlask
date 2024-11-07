from flask import Flask, request, render_template
from transformers import pipeline
import os

app = Flask(__name__)

# Lazy load the model when the user submits text
def get_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")  # Using a smaller model

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    if request.method == "POST":
        text = request.form["text"]
        summarizer = get_summarizer()
        summary = summarizer(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
