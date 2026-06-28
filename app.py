from flask import Flask, render_template, request
import os
from PyPDF2 import PdfReader
from res import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Extract text from PDF
def extract_text(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["resume"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    resume_text = extract_text(filepath)

    result = analyze_resume(resume_text)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)