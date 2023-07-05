#20.01
"""
В одну склянку налито вино, а в іншу - таку ж кількість води.
Зі склянки з вином беруть чайну ложку вина й переливають її в склянку з водою.
Потім, добре перемішавши вміст склянки з водою, беруть чайну ложку розчину і переливають її назад у склянку з вином.
Чого при цьому виявляється більше - вина у воді або води у вині?
"""

cup_capcity = 100.0
spoon_capcity = 1.0

vine_cup = [cup_capcity, 0.0]
water_cup = [0.0, cup_capcity]


def spoon_fill(cup:list):
    f = sum(cup)
    spoon = []

    for liquid in cup:
        spoon.append(liquid * (spoon_capcity / f))
    
    return spoon


def cup_minus(cup:list, spoon:list):
    for liq in range(len(cup)):
        cup[liq] -= spoon[liq]

    return cup


def cup_plus(cup:list, spoon:list):
    for liq in range(len(cup)):
        cup[liq] += spoon[liq]

    return cup


def func(cupA:list, cupB:list):
    spoon = spoon_fill(cupA)
    cupA = cup_minus(cupA, spoon)
    cupB = cup_plus(cupB, spoon)

    spoon = spoon_fill(cupB)
    cupB = cup_minus(cupB, spoon)
    cupA = cup_plus(cupA, spoon)

    return cupA, cupB


if __name__ == '__main__':
    print("After", vine_cup, water_cup)
    vine_cup, water_cup = func(vine_cup, water_cup)
    print("Before", vine_cup, water_cup)
    water_cup.reverse()

    if vine_cup == water_cup:
        print("Cups is equil")