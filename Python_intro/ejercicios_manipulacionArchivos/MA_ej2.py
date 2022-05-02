##### **Ejercicio 2**
#Escribí un programa que lea un archivo e imprima las primeras n líneas.

def imrpimir_lineas(n_lineas):
    archivo = open("ejercicio_1.txt", "r")
    lineas = archivo.readlines()
    for i in range(0 , n_lineas):
        print (lineas[i])
    archivo.close()

imrpimir_lineas(6)

