import random
from random import shuffle
def draft():
    for i in range(7):
        pkmn = input(f"{pick1} elige pick {i+1}:")
        equipo1.append(pkmn)
        print(equipo1)
        pkmn = input(f"{pick2} elige pick {i+1}:")
        equipo2.append(pkmn)
        print(equipo2)
        pkmn = input(f"{pick3} elige pick {i+1}:")
        equipo3.append(pkmn)
        print(equipo3)
        pkmn = input(f"{pick4} elige pick {i+1}:")
        equipo4.append(pkmn)
        print(equipo4)
        pkmn = input(f"{pick5} elige pick {i+1}:")
        equipo5.append(pkmn)
        print(equipo5)
        pkmn = input(f"{pick6} elige pick {i+1}:")
        equipo6.append(pkmn)
        print(equipo6)

jugador1 = input("Nombre del jugador 1:")
jugador2 = input("Nombre del jugador 2:")
jugador3 = input("Nombre del jugador 3:")
jugador4 = input("Nombre del jugador 4:")
jugador5 = input("Nombre del jugador 5:")
jugador6 = input("Nombre del jugador 6:")

aleatorio = [jugador1, jugador2, jugador3, jugador4, jugador5, jugador6]

for i in aleatorio:
    pick1 = random.choice(aleatorio)
    aleatorio.remove(pick1)
    pick2 = random.choice(aleatorio)
    aleatorio.remove(pick2)
    pick3 = random.choice(aleatorio)
    aleatorio.remove(pick3)
    pick4 = random.choice(aleatorio)
    aleatorio.remove(pick4)
    pick5 = random.choice(aleatorio)
    aleatorio.remove(pick5)
    pick6 = random.choice(aleatorio)
    aleatorio.remove(pick6)

print(pick1)
print(pick2)
print(pick3)
print(pick4)
print(pick5)
print(pick6)

equipo1 = [pick1]
equipo2 = [pick2]
equipo3 = [pick3]
equipo4 = [pick4]
equipo5 = [pick5]
equipo6 = [pick6]

draft()

print("EQUIPOS DRAFTEADOS:")
print(equipo1)
print(equipo2)
print(equipo3)
print(equipo4)
print(equipo5)
print(equipo6)


'''
jugadores=[0]
for i in range(6):
    print(input(f"Nombre del jugador {i+1}:"))
    if i == 0:
        jugadores.remove(0)
    jugadores.append(input())

print(jugadores)
shuffle(jugadores)
print(jugadores)
print(jugadores[0])
'''


'''
dicc_jugadores = {}
auxiliar = dicc_jugadores
for i in jugadores:
    dicc_jugadores[i] = {}
    dicc_jugadores = dicc_jugadores[i]

print(auxiliar)


def players():
    diccionario={}
    caste=input("Nombre del jugador 1:")
    ing=input("Pick 1:")
    return diccionario
players()




for n in range(7):

    print(f"{jugador1} introduzca pick {n+1}:")
    jugador1.append(input())
'''





