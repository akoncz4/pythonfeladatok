print("Saját függvény definiálása")
def cica():    #paraméter nélküli függvény
    return print("Ez egy köszönés")
cica()
###############
def negyzet(a):
    a=a*a
    return a
beszam=12
print("A",beszam,"négyzete: ",negyzet(beszam))
###############
def teglalap_ker(a,b):
    ker=2*(a+b)
    return ker
ta=5
tb=8
print("A téglalap kerülete: ",teglalap_ker(ta,tb))
###############
def teglalap_ker_ter(a,b):
    ker=2*(a+b)
    ter=a*b
    return (ker,ter)
print("A téglalap kerülete és területe: ",teglalap_ker_ter(ta,tb))