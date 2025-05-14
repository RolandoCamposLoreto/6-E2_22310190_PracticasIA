# Importando las librerías necesarias
import numpy as np
# Importando Counter desde la colección para contar la frecuencia de las palabras en el corpus
from collections import Counter

# Definición de la clase LanguageModel
class LanguageModel:
    def __init__(self, corpus):
        """
        Inicializa el modelo de lenguaje con el corpus de texto proporcionado.
        Calcula las frecuencias de las palabras y sus probabilidades.
        """
        self.corpus = corpus  # Almacena el corpus de texto
        # Cuenta la frecuencia de cada palabra en el corpus utilizando Counter
        self.word_counts = Counter(corpus.split())
        # Calcula el número total de palabras en el corpus
        self.total_words = len(corpus.split())
        # Calcula las probabilidades de las palabras
        self.word_probabilities = self.calculate_word_probabilities()

    def calculate_word_probabilities(self):
        """
        Calcula las probabilidades de cada palabra en el corpus.
        La probabilidad se calcula como la frecuencia de la palabra dividida por el número total de palabras.
        """
        word_probabilities = {}  # Diccionario para almacenar las probabilidades de las palabras
        # Para cada palabra y su frecuencia en el corpus
        for word, count in self.word_counts.items():
            # La probabilidad de la palabra es su frecuencia dividida por el total de palabras
            word_probabilities[word] = count / self.total_words
        return word_probabilities

    def get_probability(self, word):
        """
        Devuelve la probabilidad de una palabra. Si la palabra no está en el corpus, devuelve 0.
        """
        return self.word_probabilities.get(word, 0)

# Ejemplo de uso
# Definir un corpus de texto simple
corpus = "this is a sample corpus with some words in it this is a test"
# Crear el modelo de lenguaje con el corpus
model = LanguageModel(corpus)

# Ver probabilidad de la palabra 'this'
print("Probabilidad de 'this':", model.get_probability('this'))
