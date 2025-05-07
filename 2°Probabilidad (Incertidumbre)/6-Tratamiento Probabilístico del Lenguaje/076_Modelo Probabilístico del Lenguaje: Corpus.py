import numpy as np
from collections import Counter

class LanguageModel:
    def __init__(self, corpus):
        self.corpus = corpus
        self.word_counts = Counter(corpus.split())
        self.total_words = len(corpus.split())
        self.word_probabilities = self.calculate_word_probabilities()

    def calculate_word_probabilities(self):
        word_probabilities = {}
        for word, count in self.word_counts.items():
            word_probabilities[word] = count / self.total_words
        return word_probabilities

    def get_probability(self, word):
        return self.word_probabilities.get(word, 0)

# Ejemplo de uso
corpus = "this is a sample corpus with some words in it this is a test"
model = LanguageModel(corpus)

# Ver probabilidad de una palabra
print("Probabilidad de 'this':", model.get_probability('this'))
