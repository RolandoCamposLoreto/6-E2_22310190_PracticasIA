# Simulando el "reconocimiento de voz" con un archivo de texto

def read_text_from_file(file_path):
    """Lee el contenido de un archivo de texto"""
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado.")
        return None

# Ruta del archivo de texto (en lugar de usar un micrófono, usamos un archivo pregrabado)
text_file = "audio_transcription.txt"  # Reemplaza con el nombre del archivo en tu repositorio

# Leer el texto del archivo
recognized_text = read_text_from_file(text_file)

if recognized_text:
    print("Texto reconocido: ", recognized_text)
