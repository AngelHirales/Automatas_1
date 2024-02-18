# Practica1.5.py
# Angel Gabriel Hirales Guzman

import json

# Leer el archivo JSON
with open('ejemplo.json') as file:
    data = json.load(file)

# Convierte el diccionario a una cadena JSON
json_string = json.dumps(data, ensure_ascii=False)

# Diccionario para almacenar los tokens que se vayan generando
tokens = {}

# Asignar a cada caracter su token correspondiente
for char in json_string:
    if char == '\n':
        tokens[repr(char)] = "[ENTER]"
    else:
        unicode_valor = ord(char)
        tokens[repr(char)] = str(unicode_valor)

# Crear un archivo JSON con los tokens
nombre_archivo = "salida_tokens.txt"
with open(nombre_archivo, "w") as archivo:
    for char in json_string:
        archivo.write(f"{tokens[repr(char)]} := {repr(char)}\n")

print(f"Archivo guardado como: {nombre_archivo}")
