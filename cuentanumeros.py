# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). ><
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
numero=int(input("Introduce los numeros a introducir"))
cont=1
cero=0
negativo=0
positivo=0
while cont <= numero:
    num=int(input("Introduce el numero"))
    if (num < 0):
        negativo+=1
    elif (num == 0):
        cero+=1
    else:
        positivo+=1
    cont+=1
print ("hay ",cero," ceros")
print ("hay ",positivo," numeros positivos")
print ("hay ",negativo," numeros negativos")