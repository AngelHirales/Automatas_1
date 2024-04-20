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
        # Caracter de comillas dobles
        if char == chr(34):
            if en_comillas:
                # Fin de palabra y asignar token 999
                lista_tokens[palabra] = 999
                palabra = ''
                en_comillas = False
            else:
                # Inicio de palabra
                en_comillas = True
        elif en_comillas:
            # Agregar caracter a la palabra
            palabra += char
        else:
            # Manejar caracteres no dentro de comillas
            value = ord(char)
            lista_tokens[char] = value

    # Agregar la última palabra si no está vacía
    if palabra:
        lista_tokens[palabra] = 999

    array_tokens = list(lista_tokens.values())
    return lista_tokens, array_tokens

# imprime el contenido del archivo y sus tokens correspondientes
def imprimir_tokens(file, tokens):
    lista_tokens = {}
    palabra = ''
    en_comillas = False

    for char in file:
        # Caracter de comillas dobles
        if char == chr(34):
            if en_comillas:
                # Fin de palabra y asignar token 999
                lista_tokens[palabra] = 999
                print(f'999="{palabra}"')  # Imprimir palabra agrupada con comillas y token
                palabra = ''
                en_comillas = False
            else:
                # Inicio de palabra
                en_comillas = True

        elif en_comillas:
        # Agregar caracter a la palabra
            palabra += char

        elif char == chr(10):
            print(f'{tokens[char]}=[ENTER]')
        elif char == chr(32):
            print(f'{tokens[char]}=[ESPACIO]')
        elif char in tokens:
            print(f'{tokens[char]}={char}')

        else:
        # Manejar caracteres no dentro de comillas
            value = ord(char)
            lista_tokens[char] = value

    # Agregar la última palabra si no está vacía
    if palabra:
        lista_tokens[palabra] = 999
        print(f'999="{palabra}"')  # Imprimir palabra agrupada con comillas y token

    array_tokens = list(lista_tokens.values())
    return lista_tokens, array_tokens


# Escribir un archivo output.txt los tokens y caracteres
def escribir_archivo(file, tokens):

    with open('output.txt', 'w') as output:
        lista_tokens = {}
        palabra = ''
        en_comillas = False

        for char in file:
            # Caracter de comillas dobles
            if char == chr(34):
                if en_comillas:
                    # Fin de palabra y asignar token 999
                    lista_tokens[palabra] = 999
                    output.write(f'999="{palabra}"\n')  # Imprimir palabra agrupada con comillas y token
                    palabra = ''
                    en_comillas = False
                else:
                    # Inicio de palabra
                    en_comillas = True

            elif en_comillas:
                # Agregar caracter a la palabra
                palabra += char

            elif char == chr(10):
                # Salto de línea
                output.write(f'{tokens[char]}\n')

            elif char == chr(32):
                # Espacio en blanco
                output.write(f'{tokens[char]}\n')

            elif char in tokens:
                # Caracter normal
                output.write(f'{tokens[char]}={char}\n')

            else:
                # Manejar caracteres no dentro de comillas
                value = ord(char)
                lista_tokens[char] = value
                # Escribir el caracter directamente
                output.write(char)

        # Agregar la última palabra si no está vacía
        if palabra:
            lista_tokens[palabra] = 999
            output.write(f'999="{palabra}"\n')

        array_tokens = list(lista_tokens.values())
        return output,lista_tokens,array_tokens


# Comprueba que el archivo cargado es un json        
def validar_json(array):
        if array[0] == 123:
            True
        else:
            print('no es archivo json')
            exit(1)


# comprueba si se cerraron las comillas
def comillas_cerradas(array):
    bandera = True
    if bandera == True :
        print('\n✅Codigo JSON leido y ejecutado correctamente✅')
        exit(1)
    for valor in array:
        if valor == 34:
            bandera = not bandera
    if bandera == False:
        print("\n❌!!ERROR: Las comillas no se abrieron/cerraron correctamente!!❌")
        exit(1)


def main():
    print('-----------------------------------------------------------------------------------------------------------------------------')
    print('CONTENIDO DEL ARCHHIVO JSON: ')
    print('-----------------------------------------------------------------------------------------------------------------------------')
    
    # variable file para manejar el contenido del archivo
    file = leer_json('json_example.json')
    tokens = tokenizar(file)
    
    # mostrar el contenido del archivo
    imprimir_tokens(file, tokens)

    # generar el archivo output.txt
    escribir_archivo(file, tokens)
    
    print('----------------------------------------------------------------------------------------------------------------------------')
    print('ARRAY DE TOKENS: ')
    print('-----------------------------------------------------------------------------------------------------------------------------')
   
    # Imprime el array de los tokens
    print(array_tokens)
    
    # Imprime un error en caso de que la comilla no este cerrada
    print(comillas_cerradas(array_tokens))

if __name__ :" __main__"
main()
