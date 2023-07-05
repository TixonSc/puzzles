#17.01
"""
Діаманти і ваги
У коробці лежать 242 діаманти, з яких один природного походження, решта — його копії, виготовлені в лабораторії (штучні).
Маси штучних діамантів однакові, маса природного трохи менше.
Придумайте систему дій для виділення природного діаманта за допомогою 5-и зважувань на чашкових вагах без гир і важків.
"""

import random
import math

count_diamonds = 242
TRUE_DIAMOND = random.randint(0, count_diamonds - 1)
diamonds = [False for n in range(count_diamonds)]
diamonds[TRUE_DIAMOND] = True
turns = 1


#
def minus(arr:list, range_sub):
    return [arr.pop[i] for i in range(range_sub)]
#


def subdivane(group:list):     #sub on 3
    global turns

    sub = math.ceil(len(group) / 3)
    sub_3 = sub * 2
    index_true = group.index(True)

    print(f"\nturn:{turns}\n sub {sub} sub {sub_3} max {len(group)} <<<\tindex:{index_true + 1}")

    sub_group = []

    if index_true + 1 <= sub:
        print("Pick 1 group")
        for i in range(0, sub):
            sub_group.append(group[i])
    elif index_true + 1 >= sub_3:
        print("Pick 3 group")
        for i in range(sub_3 - 1, len(group)):
            sub_group.append(group[i])
    else:
        print("Pick 2 group")
        for i in range(sub, sub_3):
            sub_group.append(group[i])
    
    if len(sub_group) == 1:
        if sub_group[0]: return sub_group[0]
        else: return False

    turns += 1
    
    return subdivane(sub_group)



if __name__ == '__main__':
    print(subdivane(diamonds))
    print(TRUE_DIAMOND + 1)
    print(diamonds)