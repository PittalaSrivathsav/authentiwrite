import nltk
nltk.download('punkt')

def split_sentences(text):
    return nltk.sent_tokenize(text)