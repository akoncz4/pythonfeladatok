import random
lista = []
i=0
while i<10:
    vsz=random.randint(1,100)
    lista.append(vsz)
    i=i+1
print(lista)
print("Üres lista véletlen helyére véletlen szám")
lista2=[]
i=0
while i<10:
    vsz=random.randint(1,100)
    vszi=random.randint(1,100)
    print("A véletlen szám: ",vsz)
    print("Véletlen index: ",vszi)
    lista2.insert(vszi,vsz)
    i=i+1
print(lista2)