class StatisticalMachineTranslation:
    def __init__(self):
        self.translation_model = {
            'hello': 'hola',
            'world': 'mundo',
            'good': 'bueno',
            'morning': 'mañana'
        }

    def translate(self, sentence):
        words = sentence.split()
        translated = [self.translation_model.get(word, word) for word in words]
        return ' '.join(translated)

# Ejemplo de uso
stm = StatisticalMachineTranslation()
sentence = "hello world"
translated_sentence = stm.translate(sentence)
print("Frase traducida:", translated_sentence)
