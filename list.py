#lista = [5,7,2,4,8,3]
#összeg = 0
#print("A lista számai: ", lista)
#for i in lista:
    #összeg+=i
#print("A számok összege:",összeg)

most=[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
i=0
while i<len(most):
    most[i]=4
    i=i+1
for valami in most:
    print(valami)
import random
i=0
while i<len(most):
    vsz=random.randint(1,100)
    most[i]=vsz
    i=i+1  
print()
for valami in most:
    print(valami)