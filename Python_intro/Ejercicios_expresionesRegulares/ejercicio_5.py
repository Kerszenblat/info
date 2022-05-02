##### **Ejercicio 5**
#Escribí un programa que diga si un string empieza con un número específico.

def arrancar_con_numero(string, n):
    import re
    numero = "^" + n
    print(bool(re.search)(numero, string))

arrancar_con_numero("7hola", "7")


    
