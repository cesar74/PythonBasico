# Realizar un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado.><

cad=input("Intro. cadena")
subcad=input("Intro. subcadena")

if cad.find(subcad) > -1:
    print("La subcadena",subcad," está en la cadena ",cad)
else:
    print("La subcadena no está en la cadena")

# Otra forma de hacerlo
if subcad in cad:
    print("La subcadena",subcad," está en la cadena ",cad)
else:
    print("La subcadena no está en la cadena")