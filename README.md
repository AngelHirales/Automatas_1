# Compilador / Lector de archivos json
##

### Este proyecto tiene como objetivo crear un compilador/lector de archivos JSON, lo cual hace de la siguiente manera:
### Al colocar el nombre del archivo que deseas leer o ejecutar en la funcion main, este leera el contenido del archivo, asignando token unicode a cada uno de los caracteres o palabras que encuentre en el archivo json.
## -- el programa es capaz de realizar lo siguiente hasta el momento:
### 1. Lee el contenido del archivo JSON y separa los caracteres y las palabras (el contenido que se encuentra dentro de comillas dobles) asignando su valor unicode correspondiente.
### 2. Para el contenido dentro de comillas, se asigna el valor 999 como token.
### 3. Detecta si las comillas no se abren/cierran de manera correcta.
### 4. Es capaz de detectar si hay espacios o tabulaciones en el contenido del archivo.
## 
##

## -- Instrucciones para utilizar el codigo:
### 1. Tener instalado visual studio code y python en un computadora.
### descarga visual studio code aqui:
    https://code.visualstudio.com
### descarga python aqui:
    https://www.python.org/downloads/
### 2- Descarga el codigo como .zip.
### 3- coloca o crea el archivo json que deseas ejecutar en la misma carpeta donde esta el codigo.
### 4- En la funcion main cambia el nombre "json_example.txt" por el nombre del archivo que deseas leer.
### 5- Ejecuta el programa por medio de la consola o en la interfaz de visual studio, obtendras una salida tanto en consola como en un archivo de texto con el nombre "output.txt", con los caracteres y su valor unicode correspondiente.
## 
##

### Comando para ejecutar el proyecto desde la consola:
```bash
python compilador_json.py
```

### En caso de que el anterior comando no funcione, intenta con este:
```bash
python3 compilador_json.py
```
