import math

a = float(input("Add meg az A oldal hosszát: "))
b = float(input("Add meg a B oldal hosszát: "))
c = float(input("Add meg a C oldal hosszát: "))
m = float(input("Add meg a háromszög magasságát: "))
def harosz_k_t(a, b, c, m):
    kerulet = a + b + c
    terulet = (a * m) / 2
    return (kerulet, terulet)
kerulet, terulet = harosz_k_t(a, b, c, m)
print("A háromszög kerülete és területe: ", kerulet, terulet)
atmero = float(input("Add meg a kör átmérőjét: "))
sugar = atmero / 2
def kor_k_t(sugar):
    k = 2 * sugar * math.pi
    t = math.pow(sugar, 2) * math.pi
    return (k, t)
k, t = kor_k_t(sugar)
print("A kör kerülete és területe: ", k, t)