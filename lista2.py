# Nota media ><
notas = []
for indice in range(1,6):
    while True:
        valor=int(input("intro nota %d:" % indice))
        if valor >= 0 and valor <=10: break
    notas.append(valor)

print("notas: ",end="")
for nota in notas:
    print(nota," ",end="")
print("Nota media: ",sum(notas)/len(notas))
print("Nota maxima: ",max(notas))
print("Nota minima: ",min(notas))

