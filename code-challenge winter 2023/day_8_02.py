#18.01
"""
До вечері — три підсмажених скибочки
Мама дуже смачно підсмажує скибочки хліба, користуючись спеціальною маленькою сковорідкою.
Підсмаживши одну сторону кожної скибочки, вона перевертає її на іншу сторону.
Підсмажування кожної сторони скибочки триває 30 секунд, причому на сковорідці вміщується поруч тільки дві скибочки.
Зметикуйте, яким чином при цих умовах мама підсмажує обидві сторони трьох скибочок тільки за 1½ хвилини, а не за 2.
"""

BREADS = 3
BREAD_SIDES = 2
FRYING_PAN_SIZE = 2
TIME_OVER = 1.5
TIME_FRYING = 0.5
MAX_TURNS = int(TIME_OVER // TIME_FRYING)

breads = [i for i in range(1, BREADS + 1)]
frying_plan = [[0 for i in range(FRYING_PAN_SIZE)] for n in range(MAX_TURNS)]


def is_ok_plan(plan:list[list]):
    for turn in plan:
        if turn[0] == turn[1]: return False
    
    for bread in breads:
        if frying_plan.count(bread) > BREAD_SIDES: return False

    return True


def create_plan():
    plan = [[0 for i in range(FRYING_PAN_SIZE)] for n in range(MAX_TURNS)]
    pickem = breads
    this = 0
    for turn in range(len(plan)):
        pickem = breads

        for bread in breads:
            if pickem.count(bread) == BREAD_SIDES: pickem.pop(breads.index(bread))

        for place in range(len(plan[turn])):
            plan[turn][place] = pickem[this]
            this = 0 if len(pickem) - 1 == this else this + 1

    return plan

if __name__ == '__main__':
    plan = create_plan()
    if is_ok_plan(plan): print(plan)
    else: print("shit")
    print(breads)