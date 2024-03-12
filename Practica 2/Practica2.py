# Practica 2.py
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
        tokens[repr(char)] = "[SALTO_LINEA]"
    else:
        unicode_valor = ord(char)
        tokens[repr(char)] = str(unicode_valor)

# Variables para agrupar palabras dentro de comillas dobles
en_comillas = False
palabra_actual = ""

# Lista para almacenar las palabras agrupadas con su token
palabras = []

# Ciclo para agrupar los caracteres dentro de las comillas
for char in json_string:
    if char == '"':
        if en_comillas:
            en_comillas = False
            palabras.append(('"', '34'))  # Comillas como tokens separados
            palabras.append((palabra_actual, "999"))
            palabra_actual = ""
        else:
            en_comillas = True
            palabras.append(('"', '34'))  # Comillas como tokens separados
    elif en_comillas:
        palabra_actual += char
    else:
        if palabra_actual:
            palabras.append((palabra_actual, tokens[repr('"')]))
            palabra_actual = ""
        palabras.append((char, tokens[repr(char)]))

# Crear un archivo JSON con los tokens asignados a los caracteres
nombre_archivo = "salida_tokens.txt"
with open(nombre_archivo, "w") as archivo:
    for palabra, token in palabras:
        archivo.write(f"{token} := {palabra}\n")

print(f"Archivo guardado como: {nombre_archivo}")