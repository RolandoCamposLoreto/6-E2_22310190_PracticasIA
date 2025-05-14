# Definición de la clase StatisticalMachineTranslation que realiza traducción de texto
class StatisticalMachineTranslation:
    def __init__(self):
        """
        Inicializa el modelo de traducción con un diccionario simple de traducción de palabras.
        El diccionario contiene pares de palabras en inglés como clave y su traducción en español como valor.
        """
        # Modelo de traducción con algunas palabras predefinidas
        self.translation_model = {
            'hello': 'hola',
            'world': 'mundo',
            'good': 'bueno',
            'morning': 'mañana'
        }

    def translate(self, sentence):
        """
        Traduce una frase del inglés al español utilizando el modelo de traducción.
        Si la palabra no está en el modelo, la deja tal cual está en la frase original.
        """
        # Divide la oración en palabras usando 'split()'
        words = sentence.split()
        # Traduce cada palabra de la oración, usando el diccionario de traducción o dejando la palabra tal cual si no está en el diccionario
        translated = [self.translation_model.get(word, word) for word in words]
        # Une las palabras traducidas de nuevo en una oración
        return ' '.join(translated)

# Ejemplo de uso
# Crear una instancia de la clase StatisticalMachineTranslation
stm = StatisticalMachineTranslation()
# Frase a traducir del inglés al español
sentence = "hello world"
# Llamar al método 'translate' para traducir la frase
translated_sentence = stm.translate(sentence)
# Imprimir la frase traducida
print("Frase traducida:", translated_sentence)
