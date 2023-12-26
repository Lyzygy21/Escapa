import nltk
nltk.download('punkt')

def tokenize(text):
    return nltk.word_tokenize(text)