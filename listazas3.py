import random
lista = []
i=0
while i<10:
    vsz=random.randint(1,100)
    lista.append(vsz)
    i=i+1
print(lista)
#A lista legnagyobb eleme
maximum=lista[0]       #a listából veszek egy értéket
i=0                #ckilusváltozó értékének beállítása
while i<len(lista):     #ciklus végig a lista minden elemén
    if maximum<lista[i]:     #ha a max változó értéke kisebb, mint a lista adott eleme
        maximum=lista[i]     #tegye egyenlőve a max változó értékét a lista adott elemével
    i=i+1                #ciklusváltozó értékének növelése
print("A legnagyobb szám: ", maximum)    #készen vagyunk
print("A lista legnagyobb értéke: ", max(lista))
#a legkisebb elem kiválasztása
mini=lista[0]
i=0
while i<len(lista):
    if mini>lista[i]:
        mini=lista[i]
    i=i+1
print("A legkisebb szám: ", mini)
print("A lista legkisebb eleme: ", min(lista))