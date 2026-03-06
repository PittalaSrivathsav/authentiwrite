import PyPDF2

def read_file(file):

    filename = file.filename.lower()

    text = ""

    if filename.endswith(".txt"):
        text = file.read().decode("utf-8")

    elif filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    return text.strip()