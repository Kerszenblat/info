
##### **Ejercicio 8**
#Escribí un programa que separe y devuelva los caracteres númericos de un string.

def separar_numeros(string):
    import re
    separar = re.findall(r'\d', string)
    for num in separar:
        print(num)

separar_numeros("laraker1234")