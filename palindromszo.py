szo = input("Adj meg egy szót: ")
hossz = len(szo)
ekezet = "áéíóöőúüű"
nemekezet = "aeiooouuu"
csere = str.maketrans(ekezet, nemekezet)
cserelt = szo.translate(csere)
palindrom = True
for i in range(hossz):
    if szo[i] != szo[hossz - i - 1]:
        palindrom = False
if palindrom:
    print(cserelt, "palindrom szó")
else:
    print(cserelt, "nem palindrom szó")