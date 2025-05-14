# Simulando el "reconocimiento de voz" con un archivo de texto

def read_text_from_file(file_path):
    """Lee el contenido de un archivo de texto"""
    try:
        # Intentamos abrir el archivo en modo lectura
        with open(file_path, 'r') as file:
            text = file.read()  # Leemos todo el contenido del archivo
        return text  # Devolvemos el texto leído
    except FileNotFoundError:
        # Si el archivo no existe, mostramos un mensaje de error
        print(f"El archivo {file_path} no fue encontrado.")
        return None  # Si no se encuentra el archivo, devolvemos None

# Ruta del archivo de texto (en lugar de usar un micrófono, usamos un archivo pregrabado)
text_file = "audio_transcription.txt"  # Reemplaza con el nombre del archivo en tu repositorio

# Leer el texto del archivo
recognized_text = read_text_from_file(text_file)

if recognized_text:
    # Si el texto fue leído correctamente, lo imprimimos
    print("Texto reconocido: ", recognized_text)
