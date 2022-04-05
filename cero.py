# Programa que vaya pidiendo numeros y que cuando se introduzca un cero
# Entienda que es el fin, muestre la suma y su media. ><
num=1
sum=0
cont=1
while (num!=0):
    num=int(input("Introduzca un numero"))
    sum=sum+num
    if (cont==1 and num==0):
        media=0
        break
    cont+=1
media=sum/(cont-1)
print("Introduciste ",cont," numeros")
print("la media es:",media)
print("la suma es:",sum)