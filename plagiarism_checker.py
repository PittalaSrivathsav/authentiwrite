from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

nltk.download('punkt')

reference_sources = [
    "Artificial intelligence is transforming modern education.",
    "Students use online resources for assignments and research.",
    "Machine learning enables computers to learn from data."
]

def check_plagiarism(text):

    sentences = nltk.sent_tokenize(text)

    suspicious = []
    plagiarism_count = 0

    for sentence in sentences:

        documents = reference_sources + [sentence]

        vectorizer = TfidfVectorizer().fit_transform(documents)

        similarity_matrix = cosine_similarity(vectorizer)

        scores = similarity_matrix[-1][:-1]

        similarity_score = max(scores)

        # 🔴 Strong plagiarism
        if similarity_score > 0.65:

            suspicious.append({
                "text": sentence,
                "color": "red"
            })

            plagiarism_count += 1

        # 🟡 Suspicious similarity
        elif similarity_score > 0.40:

            suspicious.append({
                "text": sentence,
                "color": "yellow"
            })

    plagiarism_score = round((plagiarism_count / max(len(sentences),1)) * 100,2)

    return plagiarism_score, suspicious