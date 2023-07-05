#12.01
"""
 «Допоможи рибалкам не посваритися»

   Умова задачі: Після шторму троє рибалок знайшли викинуті на берег бочки з вином, сім з них були пусті, сім – напівпусті, а ще сім – повні.
   Як їм поділити свій скарб порівну на трьох, щоб кожному дісталася рівна кількість бочок і порівну вина?

   Обов’язкова умова розв’язання: рибалкам не можна переливати вино з бочки в бочку!

   Для вирішення завдання, визначити логіку та послідовність подій.
"""
COUNT_OF_FISHERS = 3
COUNT_OF_BARRELS = 7
EMPTY = 0.0
HALF = 0.5
FULL = 1.0

fishermans = [[] for i in range(COUNT_OF_FISHERS)]
barrels = []

for barrel in range(COUNT_OF_BARRELS):
    barrels.append(EMPTY)
    barrels.append(HALF)
    barrels.append(FULL)

NEED = [len(barrels) // COUNT_OF_FISHERS, COUNT_OF_BARRELS * (HALF + FULL) / COUNT_OF_FISHERS]


def give_pls(need):
    for barrel in barrels:
        if barrel == need: return barrels.pop(barrels.index(barrel))

    if need >= FULL:
        for barrel in barrels:
            if barrel == HALF: return barrels.pop(barrels.index(barrel))

        for barrel in barrels:
            if barrel == EMPTY: return barrels.pop(barrels.index(barrel))
    
    else:
        print("SHIT!")
        return None


if __name__ == '__main__':

    while len(barrels):

        for fisher in fishermans:
            left_barrels, left_vine = [NEED[0] - len(fisher), NEED[1] - sum(fisher)]
            barrel:float

            if left_barrels == left_vine == 0: continue
            if left_barrels > 0:
                if left_vine == 0.0: barrel = give_pls(EMPTY) #only empty
                if left_vine == 0.5: barrel = give_pls(HALF) #only half
                if left_vine >= 1.0: barrel = give_pls(FULL) #half or full
            elif left_barrels == 0 and left_vine > 0.0: pass #shit

            fisher.append(barrel)

    print(f"fisers{fishermans}\nbarrels{barrels}")