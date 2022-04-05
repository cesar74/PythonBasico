# ><
cadena=input("introduce la cadena:")
num=0
cont=0
while num <= 0 or num > len(cadena):
    num=int(input("introduce el caracter a mostrar de la cadena"))
print (cadena[0:num])

