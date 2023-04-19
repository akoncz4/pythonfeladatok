print("FOR ciklus")
print("A FOR ciklus általában előre meghatározott lépésszámú")
neve=[2,4,3,2,1]
print(neve)
for i in range(len(neve)):
    print(neve[i])
print("Számoljunk el 10-ig")
for i in range(10):
    print(i)
print("Számoljunk el 1-től 10-ig")
for i in range(1,10):
    print(i)
print("Számoljunk el 10-től 1-ig")
for i in range(10,0,-1):
    print(i)
print("Számoljunk el 1-től 10-ig, 2-vel")
for i in range(0,10,2):
    print(i)
print("A lista minden második elemét írjuk ki")
for i in range(0,len(neve),2):
    print(neve[i])
print("A lista minden második elemét írjuk ki visszafelé")
for i in range(len(neve)-1,-1,-2):
    print(neve[i])
print("Szövegben for")
s="Hello, szia, szevasz"
for i in range(len(s)):
    print(s[i])
print("Ahogy a Python csinálja")
for i in s:
    print(i, end=" ")
print("Ahogy a Python csinálja (minden 2. karaktert írja ki)")
for i in range(0,len(s),2):
    print(s[i])
szoveg=str(input("Írj be egy szöveget, a program ki fogja írni visszafele: "))
for i in range(len(szoveg)):
    print(szoveg[i], end=" ")