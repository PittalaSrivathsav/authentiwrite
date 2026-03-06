import nltk
import numpy as np

nltk.download('punkt')

def generate_suggestions(text):

    suggestions = []

    sentences = nltk.sent_tokenize(text)
    words = text.split()

    if len(words) == 0:
        return suggestions

    unique_words = len(set(words))
    diversity = unique_words / len(words)

    sentence_lengths = [len(s.split()) for s in sentences]

    avg_length = np.mean(sentence_lengths)

    variation = np.std(sentence_lengths)

    # Suggest adding personal ideas
    if "I" not in text and "my" not in text:
        suggestions.append("Try adding personal examples or opinions to make the writing more original.")

    # Vocabulary diversity suggestion
    if diversity < 0.5:
        suggestions.append("Use more diverse vocabulary to improve authenticity.")

    # Sentence variation suggestion
    if variation < 3:
        suggestions.append("Vary your sentence lengths for more natural writing.")

    # AI-like formal tone
    if avg_length > 18:
        suggestions.append("Try simplifying some sentences to make the writing more natural.")

    return suggestions