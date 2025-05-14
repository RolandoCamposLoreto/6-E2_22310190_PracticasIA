# Importando la librería random para seleccionar aleatoriamente elementos
import random

# Definición de la clase PCFG (Grammar probabilística de contexto libre)
class PCFG:
    def __init__(self):
        """
        Inicializa la gramática probabilística de contexto libre (PCFG).
        Define las reglas de producción con sus probabilidades asociadas.
        """
        # Definir reglas de producción con probabilidades
        self.grammar = {
            # Regla para la categoría 'S' (Oración)
            'S': [('NP', 'VP', 0.9), ('Aux', 'NP', 'VP', 0.1)],  # S -> NP VP o S -> Aux NP VP con probabilidades respectivas
            # Regla para la categoría 'NP' (Sintagma nominal)
            'NP': [('Det', 'Noun', 0.7), ('ProperNoun', 0.3)],  # NP -> Det Noun o NP -> ProperNoun
            # Regla para la categoría 'VP' (Sintagma verbal)
            'VP': [('Verb', 'NP', 0.8), ('Verb', 0.2)],  # VP -> Verb NP o VP -> Verb
            # Regla para la categoría 'Det' (Determinante)
            'Det': [('a', 0.5), ('the', 0.5)],  # Det -> a o Det -> the
            # Regla para la categoría 'Noun' (Sustantivo)
            'Noun': [('dog', 0.4), ('cat', 0.6)],  # Noun -> dog o Noun -> cat
            # Regla para la categoría 'Verb' (Verbo)
            'Verb': [('chases', 0.6), ('sees', 0.4)],  # Verb -> chases o Verb -> sees
            # Regla para la categoría 'ProperNoun' (Nombre propio)
            'ProperNoun': [('John', 1.0)],  # ProperNoun -> John
            # Regla para la categoría 'Aux' (Auxiliar)
            'Aux': [('does', 1.0)]  # Aux -> does
        }

    def generate(self, non_terminal):
        """
        Genera una oración a partir de la categoría no terminal proporcionada.
        Utiliza las reglas de producción con sus probabilidades para expandir la gramática.
        """
        # Obtener las producciones posibles para el símbolo no terminal actual
        productions = self.grammar[non_terminal]
        # Seleccionar aleatoriamente una producción basada en sus probabilidades
        production = random.choices(productions, weights=[p[2] for p in productions])[0]
        # Expandir los símbolos no terminales recursivamente, generando las partes de la oración
        result = [self.generate(symbol) if symbol in self.grammar else symbol for symbol in production[:2]]
        # Unir las partes generadas en una cadena de texto
        return ' '.join(result)

# Ejemplo de uso
# Crear una instancia de la clase PCFG
pcfg = PCFG()
# Generar una oración a partir de la categoría 'S' (Oración)
sentence = pcfg.generate('S')
# Mostrar la oración generada
print("Oración generada:", sentence)
