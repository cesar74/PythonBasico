## Suponiendo que hemos introducido una cadena por teclado que representa una frase 
## (palabras separadas por espacios), realiza un programa que cuente cuantas 
## palabras tiene.

cont=0
posicion=0
cadena=input("Introduce una frase:")
# Elimino los espacios que hubiera al inicio y final de la cadena
cadena=cadena.strip()
# Voy buscando los espacios
posicion=cadena.find(" ",posicion)
while posicion != -1:
    cont+=1
    # No tengo en cuenta los posibles espacios que hay entre las palabras
    while cadena[posicion+1] == " ":
        posicion+=1
    posicion=cadena.find(" ", posicion + 1)
print("la frase tiene ",cont + 1,"palabras")
    
