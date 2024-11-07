from flask import Flask, request, render_template, jsonify
from utils.summarizer import summarize_text
from utils.pdf_handler import extract_text_from_pdf
from utils.doc_handler import extract_text_from_doc
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = ""
    
    # Check if text is provided directly
    if 'text' in request.form and request.form['text'].strip():
        text = request.form['text'].strip()
    
    # Handle file upload for PDF or DOC
    elif 'file' in request.files:
        file = request.files['file']
        if file.filename.endswith('.pdf'):
            text = extract_text_from_pdf(file)
        elif file.filename.endswith('.docx'):
            text = extract_text_from_doc(file)
        else:
            return jsonify({"error": "Unsupported file format"}), 400

    if not text:
        return jsonify({"error": "No valid text provided"}), 400

    # Generate the summary
    summary = summarize_text(text)
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)