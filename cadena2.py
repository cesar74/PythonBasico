# Pide una cadena y un caracter por teclado. Valida que sea un caracter
# Y muestra cuantas veces aparece dicho caracter en la cadena.

cadena=input("Introduce la cadena:")
longitud=2
while longitud != 1:
    caracter=input("Introduce un caracter válido")
    longitud=len(caracter)
print("el caracter ",caracter," se encuentra ,",cadena.count(caracter) ," veces")