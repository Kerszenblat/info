##### **Ejercicio 3**
"""Creá un programa que verifique las siguientes condiciones:
    
* si un string dado tiene una _h_ seguida de ninguna o más _e_.

* si un string dado tiene una _h_ seguida de una o más _e_.

* si un string dado tiene una _h_ seguida de una o más _e_.

* si un string dado tiene una _h_ seguida de dos o tres _e_.
"""

def verificar(string):
    import re 
    h1 = re.search(r"he*" , string)      # *es cero o mas veces 
    h2 = re.search(r"he+", string)       # + es una o mas veces 
    h3 = re.search(r"he{2, 3}", string)  # {} es el rango de dos o mas veces 
    print(h1, h2, h3)

verificar("helado")

