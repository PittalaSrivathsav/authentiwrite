import numpy as np
import nltk

nltk.download('punkt')

def detect_ai(text):

    if not text or len(text.strip()) == 0:
        return 0, 0, []

    sentences = nltk.sent_tokenize(text)

    if len(sentences) == 0:
        return 0, 0, []

    words = text.split()
    total_words = len(words)

    if total_words == 0:
        return 0, 0, []

    unique_words = len(set(words))

    diversity = unique_words / total_words

    sentence_lengths = [len(s.split()) for s in sentences]

    avg_length = np.mean(sentence_lengths)

    variation = np.std(sentence_lengths)

    # AI probability
    ai_score = (avg_length * 0.3) + (diversity * 100 * 0.7)

    ai_probability = min(ai_score, 100)

    # rewriting risk
    rewriting_score = ((1 - diversity) * 100) + ((5 - variation) * 5)

    rewriting_risk = max(0, min(rewriting_score, 100))

    rewritten_sentences = []

    # improved detection
    for s in sentences:

        length = len(s.split())

        # detect formal rewritten sentences
        if length > 10 or "significantly" in s.lower() or "frequently" in s.lower():
            rewritten_sentences.append(s)

    return round(ai_probability, 2), round(rewriting_risk, 2), rewritten_sentences