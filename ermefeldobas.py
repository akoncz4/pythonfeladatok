import random

while True:
    number_of_throws = int(input("Hány dobást szeretne végrehajtani? "))
    if number_of_throws > 0:
        break
    print("A dobások számának pozitív számnak kell lennie!")

fej = 0
iras = 0

for i in range(number_of_throws):
    coin = random.randint(0, 1)
    if coin == 0:        
        print("Fej")
        fej += 1
    else:
        print("Írás")
        iras += 1
print("Fej: ", fej)
print("Írás: ", iras)