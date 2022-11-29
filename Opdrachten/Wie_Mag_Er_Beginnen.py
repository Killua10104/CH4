import random

start_spelers = int(input("Hoeveel spelers zijn er?"))
spelers = []
for i in range (start_spelers):
    spelers.append(input("Speler naam: "))


print("Deze speler mag beginnen:", random.choice(spelers))