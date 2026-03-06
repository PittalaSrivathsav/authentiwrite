from flask import Flask, render_template, request
from plagiarism_checker import check_plagiarism
from ai_detector import detect_ai
import PyPDF2
import os

app = Flask(__name__)


def read_uploaded_file(file):

    filename = file.filename.lower()
    text = ""

    try:

        if filename.endswith(".txt"):
            text = file.read().decode("utf-8", errors="ignore")

        elif filename.endswith(".pdf"):

            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + " "

    except Exception as e:
        print("File reading error:", e)

    return text.strip()


# HOME PAGE
@app.route("/")
def home():
    return render_template("home.html")


# ANALYZER PAGE
@app.route("/analyze", methods=["GET", "POST"])
def analyze():

    result = None

    if request.method == "POST":

        text = request.form.get("text", "")
        uploaded_file = request.files.get("file")

        # Read uploaded file if provided
        if uploaded_file and uploaded_file.filename:
            file_text = read_uploaded_file(uploaded_file)

            if file_text:
                text = file_text

        if text and text.strip():

            try:

                plagiarism_score, suspicious = check_plagiarism(text)

                ai_score, rewrite_score, rewritten_sentences = detect_ai(text)

                authenticity = round(100 - ((plagiarism_score + ai_score) / 2), 2)

                suggestions = [
                    "Try adding personal examples or opinions to make the writing more original.",
                    "Vary your sentence lengths for more natural writing.",
                    "Use more diverse vocabulary."
                ]

                result = {
                    "text": text,
                    "plagiarism": plagiarism_score,
                    "ai": ai_score,
                    "rewrite": rewrite_score,
                    "rewritten": rewritten_sentences,
                    "authenticity": authenticity,
                    "suspicious": suspicious,
                    "suggestions": suggestions
                }

            except Exception as e:
                print("Analysis error:", e)

    return render_template("analyzer.html", result=result)


# RUN FLASK APP (FOR RENDER DEPLOYMENT)
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    app.run(host="0.0.0.0", port=port)
