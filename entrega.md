# ENTREGA: COMPILADOR DE JSON
##
## 

## Que hace el programa hasta el momento?
### - este programa lee el conenido de un archivo .json
### - asigna token su contenido separando los caracteres con su valor unicode.
### - para el caso de las palabras (el contenido dentro de comillas les asigna el token 999)
### - para el caso de las fechas (se les asigna el token 203).
### - para el caso de los numeros enteros asigna el token 201
### - para el caso de los numeros flotantes asigna el token 202
### - detecta si hay un ENTER en el archivo
### - detecta si hay un TAB en el archivo
### - detecta si hay un ESPACIO en el arhivo
### - detecta si hay comillas sin cerrar dentro del contenido del archivo, en caso de que si, muestra un error.
### - detecta si el primer caracter es un {, si no lo es marca un error
### - muestra la salida en consola
### - muestra la salida en un archivo con el nombre output.txt.
##

## que hace falta?
### - imprime las fechas 2 veces: una con el token 999 y otra con el token 203 lo cual debe corregirse
##

## proyecciones a futuro
### Este codigo cumple funciones basicas de un compilador, sin embargo, deberia poder analizar a futuro:
### - si la sintaxis del archivo json es correcta
### - evaluar si las fechas cumplen con el formato DD/MM/AAAA
### - evaluar si los corchetes se cierran o solo estan abierto y dar error en caso de que no esten cerrados
##

