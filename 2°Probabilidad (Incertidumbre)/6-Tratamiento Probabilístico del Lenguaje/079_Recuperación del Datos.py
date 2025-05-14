# Definición de la clase SimpleIR para un sistema de recuperación de información básico
class SimpleIR:
    def __init__(self):
        """
        Inicializa un índice vacío para almacenar las palabras y los documentos que las contienen.
        """
        self.index = {}

    def build_index(self, corpus):
        """
        Construye un índice invertido a partir del corpus de documentos.
        El índice mapea cada palabra a una lista de IDs de documentos en los que aparece.
        """
        for doc_id, doc in enumerate(corpus):
            # Recorre cada documento del corpus
            for word in doc.split():
                # Si la palabra no está en el índice, la agrega con una lista vacía
                if word not in self.index:
                    self.index[word] = []
                # Agrega el ID del documento donde aparece la palabra
                self.index[word].append(doc_id)

    def search(self, query):
        """
        Realiza una búsqueda en el índice invertido para encontrar los documentos que contienen todas las palabras de la consulta.
        """
        # Divide la consulta en palabras individuales
        query_words = query.split()
        # Inicializa los resultados con los documentos que contienen la primera palabra
        results = set(self.index.get(query_words[0], []))
        # Para las siguientes palabras, realiza una intersección de los documentos que las contienen
        for word in query_words[1:]:
            results &= set(self.index.get(word, []))
        # Devuelve los documentos que contienen todas las palabras de la consulta
        return results

# Ejemplo de uso
# Corpus de documentos (lista de cadenas de texto)
corpus = ["the cat in the hat", "the dog in the fog", "the quick brown fox"]
# Crear una instancia del sistema de recuperación de información
ir_system = SimpleIR()
# Construir el índice invertido a partir del corpus
ir_system.build_index(corpus)
# Realizar una búsqueda de documentos que contengan las palabras "the cat"
results = ir_system.search("the cat")
# Imprimir los documentos relevantes encontrados
print("Documentos relevantes:", results)
