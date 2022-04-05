# Comprobar si una segunda cadena empieza 
# por la primera cadena. Ambas pedidas por teclado.
cadena1=input("Intro. cadena1")
cadena2=input("Intro. cadena2")
if cadena1.startswith(cadena2):
    print("empieza por la cadena2")
else:
    print("NO empieza por la cadena2")