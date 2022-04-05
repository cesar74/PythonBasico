import random
lista_numeros = []
for indice in range(1,11):
    lista_numeros.append(random.randint(1,10))

for indice in lista_numeros:
    print (indice," ",indice**2," ",indice**3)
    
