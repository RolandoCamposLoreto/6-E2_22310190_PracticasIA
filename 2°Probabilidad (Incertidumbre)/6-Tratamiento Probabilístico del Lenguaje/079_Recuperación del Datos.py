class SimpleIR:
    def __init__(self):
        self.index = {}

    def build_index(self, corpus):
        for doc_id, doc in enumerate(corpus):
            for word in doc.split():
                if word not in self.index:
                    self.index[word] = []
                self.index[word].append(doc_id)

    def search(self, query):
        query_words = query.split()
        results = set(self.index.get(query_words[0], []))
        for word in query_words[1:]:
            results &= set(self.index.get(word, []))
        return results

# Ejemplo de uso
corpus = ["the cat in the hat", "the dog in the fog", "the quick brown fox"]
ir_system = SimpleIR()
ir_system.build_index(corpus)
results = ir_system.search("the cat")
print("Documentos relevantes:", results)
