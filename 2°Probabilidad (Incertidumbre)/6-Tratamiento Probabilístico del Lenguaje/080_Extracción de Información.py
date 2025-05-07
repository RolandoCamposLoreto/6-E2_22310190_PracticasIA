import re

class InformationExtraction:
    def __init__(self):
        self.date_pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'

    def extract_dates(self, text):
        return re.findall(self.date_pattern, text)

# Ejemplo de uso
text = "I have two appointments: one on 12/05/2022 and another on 15/06/2022."
ie = InformationExtraction()
dates = ie.extract_dates(text)
print("Fechas extraídas:", dates)
