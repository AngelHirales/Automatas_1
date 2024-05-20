# importar libreria para trabajar con json
import json


# Leer el archivo JSON
def leer_json(file_to_read):
    try:
        with open(file_to_read, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        # Si el archivo no existe
        print('❗El archivo no existe o su nombre no es correcto❗')
        exit(1)
    except json.JSONDecodeError as e:
        # Capturar error de codigo JSON
        print(f"❌Error: El archivo JSON no tiene un formato válido: {e}❌")
        exit(1)


# array para almacenar los tokens generados
array_tokens = []


# Asignar tokens a los caracteres dentro del archivo
def tokenizar(file):
    diccionario_tokens = {}
    for char in file:
        value = ord(char)
        diccionario_tokens[char] = value
        array_tokens.append(value)
    return diccionario_tokens


# agrupa los caracteres dentro de comillas como palabras y asigna el token 999
def tokenizar_palabra(file):
    lista_tokens = {}
    palabra = ''
    en_comillas = False

    for char in file:
        if char == chr(34):
            if en_comillas:
                lista_tokens[palabra] = 999
                palabra = ''
                en_comillas = False
            else:
                en_comillas = True
        elif en_comillas:
            palabra += char
        else:
            value = ord(char)
            lista_tokens[char] = value

    if palabra:
        lista_tokens[palabra] = 999

    array_tokens = list(lista_tokens.values())
    return lista_tokens, array_tokens 


# comprueba si se cerraron las comillas
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
        exit(1)


# Función para tokenizar fechas en formato DD/MM/AAAA
def tokenizar_fecha(array):
    tokens = []
    date_token = ''
    is_date = False
    for value in array:
        if 47 <= value <= 57:
            date_token += chr(value)
            if date_token.count('/') == 2 and len(date_token) == 10:
                tokens.append(203)
                date_token = ''
                is_date = True
        else:
            if is_date:
                is_date = False
            tokens.append(value)
    return tokens


# imprime el contenido del archivo y sus tokens correspondientes
def imprimir_tokens(file, tokens):
    lista_tokens = {}
    palabra = ''
    en_comillas = False
    consecutive_spaces = 0

    for char in file:
        if char == chr(34):
            if en_comillas:
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

    if palabra:
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

        for char in file:
            if char == chr(34):
                if en_comillas:
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

        if palabra:
            lista_tokens[palabra] = 999
            output.write(f'999="{palabra}"\n')

        array_tokens = list(lista_tokens.values())
        return output, lista_tokens, array_tokens


def main():

    print('-----------------------------------------------------------------------------------------------------------------------------')
    print('CONTENIDO DEL ARCHHIVO JSON: ')
    print('-----------------------------------------------------------------------------------------------------------------------------')
    
    # variable file para manejar el contenido del archivo
    file = leer_json('json_example.json')
    tokens = tokenizar(file)

    # If quotes are balanced, continue with processing
    imprimir_tokens(file, tokens)
    escribir_archivo(file, tokens)

    print('-----------------------------------------------------------------------------------------------------------------------------')
    print('ARRAY DE TOKENS: ')
    print('-----------------------------------------------------------------------------------------------------------------------------')

    # Imprime el array de los tokens
    print(array_tokens)

    # si las comillas no estan cerradas muestra el error
    print(comillas_cerradas(array_tokens))

if __name__ :" __main__"
main()
