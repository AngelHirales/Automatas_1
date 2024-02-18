# Practica1.py
# Angel Gabriel Hirales Guzman

# Crear programa que lea un archivo json eh imprima los caracteres por separado.

# importar la libreria necesaria para reconocer archivos json
import json

# Leer el archivo json
with open('ejemplo.json') as file:
    data = json.load(file)

# Convierte el diccionario a una cadena json
json_string = json.dumps(data, ensure_ascii=False)

# separa los caracteres y los imprime
for char in json_string:
    if char == '\n':
        print("[ENTER]")
    elif char == ' ':
        print("[ESPACIO]")
    elif char == ':':
        print(":")
    else:
        print(char)
