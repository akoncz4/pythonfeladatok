varos=["Mátészalka", "Nyíregyháza", "Vásárosnamény", "Kisvárda", "Debrecen"]
irsz=[4700, 4900, 4800, 4755, 4400]
vnev=str(input("Kérem a város nevét: "))
i=0
while i<len(varos):
    if varos[i]==vnev:
        print("A város neve: ", vnev)
        print("irányítószáma: ", irsz[i])
    i=i+1
if vnev not in varos:
    print("Ez a város nem szerepel a listában")