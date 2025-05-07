import random

class PCFG:
    def __init__(self):
        # Definir reglas de producción con probabilidades
        self.grammar = {
            'S': [('NP', 'VP', 0.9), ('Aux', 'NP', 'VP', 0.1)],
            'NP': [('Det', 'Noun', 0.7), ('ProperNoun', 0.3)],
            'VP': [('Verb', 'NP', 0.8), ('Verb', 0.2)],
            'Det': [('a', 0.5), ('the', 0.5)],
            'Noun': [('dog', 0.4), ('cat', 0.6)],
            'Verb': [('chases', 0.6), ('sees', 0.4)],
            'ProperNoun': [('John', 1.0)],
            'Aux': [('does', 1.0)]
        }

    def generate(self, non_terminal):
        # Selección aleatoria de una producción basada en probabilidades
        productions = self.grammar[non_terminal]
        production = random.choices(productions, weights=[p[2] for p in productions])[0]
        result = [self.generate(symbol) if symbol in self.grammar else symbol for symbol in production[:2]]
        return ' '.join(result)

# Ejemplo de uso
pcfg = PCFG()
sentence = pcfg.generate('S')
print("Oración generada:", sentence)
