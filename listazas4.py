import random
hossz=int(input("Add meg a lista hosszát: "))
lista=[]
a=0
b=int(input("Add meg a maximum számot: "))
i=0
while i<10:
    vsz=random.randint(a,b)
    lista.append(vsz)
    i=i+1
print(lista)
összeg=0
for szám in lista:
    összeg+=szám
print("A lista elemeinek összege: ", összeg)
print("A legkisebb szám: ", min(lista))
print("A legnagyobb szám: ", max(lista))