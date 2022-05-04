##### **Ejercicio 7**
#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

def encontrar_string(string):
    import re
    encuentro = re.findall(r'\w*\s*', string)
    print(encuentro)

encontrar_string("nsss2341   dd 103 ddnwd")