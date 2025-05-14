# Importa el módulo 're' que permite trabajar con expresiones regulares
import re

# Definición de la clase InformationExtraction para extraer información de texto
class InformationExtraction:
    def __init__(self):
        """
        Inicializa el patrón de expresión regular para buscar fechas en formato 'dd/mm/yyyy'.
        """
        # Patrón de expresión regular para detectar fechas en formato 'dd/mm/yyyy'
        self.date_pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'

    def extract_dates(self, text):
        """
        Extrae todas las fechas en formato 'dd/mm/yyyy' del texto proporcionado.
        """
        # Utiliza re.findall() para buscar todas las coincidencias que correspondan al patrón de fechas
        return re.findall(self.date_pattern, text)

# Ejemplo de uso
# Texto en el que se buscarán las fechas
text = "I have two appointments: one on 12/05/2022 and another on 15/06/2022."
# Crear una instancia de la clase InformationExtraction
ie = InformationExtraction()
# Llamar al método 'extract_dates' para extraer las fechas del texto
dates = ie.extract_dates(text)
# Imprimir las fechas extraídas
print("Fechas extraídas:", dates)
