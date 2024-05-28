# importar libreria para trabajar con json
import json

# ayuda:
# token para palabra = 999
# token para fecha = 203
# token numeros enteros = 201
# token numeros flotantes = 202

# Leer el archivo JSON
def leer_json(file_to_read):
    try:
        with open(file_to_read, 'r') as file:
            data = file.read()
            # Verificar que el primer caracter sea '{' (valor Unicode 123)
            if data and ord(data[0]) != 123:
                print('❌Error: El archivo JSON no comienza con "{"❌')
                exit(1)
        return data
    except FileNotFoundError:
        print('❗El archivo no existe o su nombre no es correcto❗')
        exit(1)
    except json.JSONDecodeError as e:
        print(f"❌Error: El archivo JSON no tiene un formato válido:{e}❌")
        exit(1)


# Array para almacenar los tokens
array_tokens = []

# Asignar tokens a los caracteres dentro del archivo
def tokenizar(file):
    diccionario_tokens = {}
    for char in file:
        value = ord(char)
        diccionario_tokens[char] = value
        array_tokens.append(value)
    return diccionario_tokens

# Verificar si una cadena es una fecha en formato DD/MM/AAAA
def es_fecha(cadena):
    if len(cadena) == 10 and cadena[2] == '/' and cadena[5] == '/':
        dia, mes, año = cadena.split('/')
        if dia.isdigit() and mes.isdigit() and año.isdigit():
            return True
    return False


# Imprime el contenido del archivo y sus tokens correspondientes
def imprimir_tokens(file, tokens):
    lista_tokens = {}
    palabra = ''
    en_comillas = False
    consecutive_spaces = 0

    i = 0
    while i < len(file):
        char = file[i]
        if char == chr(34):  # Manejar comillas
            if en_comillas:
                if es_fecha(palabra):
                    lista_tokens[palabra] = 203
                    print(f'203="{palabra}"')
                if palabra.isdigit():  # Verificar si es un número entero
                    lista_tokens[palabra] = 201
                    print(f'201="{palabra}"')
                elif '.' in palabra and all(part.isdigit() for part in palabra.split('.')):  # Verificar si es un número flotante
                    lista_tokens[palabra] = 202
                    print(f'202="{palabra}"')
                else:
                    lista_tokens[palabra] = 999
                    print(f'999="{palabra}"')
                palabra = ''
                en_comillas = False
            else:
                en_comillas = True
        elif en_comillas:
            palabra += char
        elif char == '\n':
            print(f'{tokens[char]}=[ENTER]')
        elif char == ' ':
            consecutive_spaces += 1
            if consecutive_spaces == 4:
                print(f'{tokens[char]}=[TAB]')
                consecutive_spaces = 0
        elif char in tokens:
            print(f'{tokens[char]}={char}')
        else:
            value = ord(char)
            lista_tokens[char] = value
        i += 1

    if palabra:
        if es_fecha(palabra):
                    lista_tokens[palabra] = 203
                    print(f'203="{palabra}"')
        if palabra.isdigit():
            lista_tokens[palabra] = 201
            print(f'201="{palabra}"')
        elif '.' in palabra and all(part.isdigit() for part in palabra.split('.')):
            lista_tokens[palabra] = 202
            print(f'202="{palabra}"')
        else:
            lista_tokens[palabra] = 999
            print(f'999="{palabra}"')

    array_tokens = list(lista_tokens.values())
    return lista_tokens, array_tokens

# Escribir un archivo output.txt los tokens y caracteres
def escribir_archivo(file, tokens):
    with open('output.txt', 'w') as output:
        lista_tokens = {}
        palabra = ''
        en_comillas = False
        consecutive_spaces = 0

        i = 0
        while i < len(file):
            char = file[i]
            if char == chr(34):  # Manejar comillas
                if en_comillas:
                    if es_fecha(palabra):
                        lista_tokens[palabra] = 203
                        output.write(f'203="{palabra}"\n')
                    else:
                        lista_tokens[palabra] = 999
                        output.write(f'999="{palabra}"\n')
                    palabra = ''
                    en_comillas = False
                else:
                    en_comillas = True
            elif en_comillas:
                palabra += char
            elif char == '\n':
                output.write(f'{tokens[char]}=[ENTER]\n')
            elif char == ' ':
                consecutive_spaces += 1
                if consecutive_spaces == 4:
                    output.write(f'{tokens[char]}=[TAB]\n')
                    consecutive_spaces = 0
            elif char in tokens:
                output.write(f'{tokens[char]}={char}\n')
            else:
                value = ord(char)
                lista_tokens[char] = value
                output.write(char)
            i += 1

        if palabra:
            if es_fecha(palabra):
                lista_tokens[palabra] = 203
                output.write(f'203="{palabra}"\n')
            else:
                lista_tokens[palabra] = 999
                output.write(f'999="{palabra}"\n')

        array_tokens = list(lista_tokens.values())
        return output, lista_tokens, array_tokens

def comillas_cerradas(array):
    bandera = False
    for valor in array:
        if valor == 34:
            bandera = not bandera
    if bandera:
        print("\n❌!!ERROR: Las comillas no se abrieron/cerraron correctamente!!❌")
        exit(1)
    else:
        print('\n✅Codigo JSON leido y ejecutado correctamente✅')

def main():
    print('-----------------------------------------------------------------------------------------------------------------------------')
    print('CONTENIDO DEL ARCHIVO JSON: ')
    print('-----------------------------------------------------------------------------------------------------------------------------')
    
    # Variable file para manejar el contenido del archivo
    file = leer_json('json_example.json')
    tokens = tokenizar(file)

    imprimir_tokens(file, tokens)
    escribir_archivo(file, tokens)

    print('-----------------------------------------------------------------------------------------------------------------------------')
    print('ARRAY DE TOKENS: ')
    print('-----------------------------------------------------------------------------------------------------------------------------')

    # Imprime el array de los tokens
    print(array_tokens)

    # Si las comillas no están cerradas muestra el error
    comillas_cerradas(array_tokens)

if __name__ == "__main__":
    main()
