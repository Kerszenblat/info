##### **Ejercicio 7**
#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir 
# y decir cuantos caracteres tiene.

def mas_larga():
    caracteres = 0
    palabras = ''
    with open("ejercicio_1.txt", "r") as archivo:
        for palabra in archivo.read().split():
            if(len(palabra) > caracteres):
                caracteres = len(palabra)
                palabra_ = palabra 
        return print(palabra_, caracteres)

mas_larga()