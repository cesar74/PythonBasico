# Calcular el factorial de un numero.><
numero=int(input("Introduce numero: "))
acumulador=1
numero1=numero
while (numero1 > 0):
    acumulador=acumulador*numero1
    numero1-=1
print("El factorial de ",numero," es ",acumulador)