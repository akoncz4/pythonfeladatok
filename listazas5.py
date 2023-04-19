import random
lista=[]
while len(lista)<10:
    vsz=random.randint(1,100)   
    if vsz%2==0:
        lista.append(vsz)
print(lista)
lista1=[]
while len(lista1)<10:
    vsz1=random.randint(1,100)
    if vsz1%2!=0:
        lista1.append(vsz1)
print(lista1)
lista2=[]
while len(lista2)<10:
    vsz2=random.randint(1,100)   
    if vsz2%3==0:
        lista2.append(vsz2)
print(lista2)
lista3=[]
while len(lista3)<10:
    vsz3=random.randint(1,100)   
    if vsz3%3==0 and vsz3%5==0:
        lista3.append(vsz3)
print(lista3)
listahossz=random.randint(1,15)
lista4=[]
kezdoertek=random.randint(1,20)
maxertek=random.randint(20,100)
while len(lista4)<listahossz:
    ertek=random.randint(kezdoertek, maxertek)
    lista4.append(ertek)
atlag=sum(lista4)/len(lista4)
i=0
while i<len(lista4) - 1:
    j=i+1
    while j<len(lista4):
        if lista4[i] > lista4[j]:
            lista4[i], lista4[j]=lista4[j], lista4[i]
        j+=1
    i+=1
print("A lista elemei(sorba rendezve): ",lista4)
print("A legkisebb érték: ", min(lista4))
print("A legnagyobb érték: ", max(lista4))
print("A lista összege: ", sum(lista4))
print("A lista átlaga: ", round(atlag))