#18.01
"""
До вечері — три підсмажених скибочки
Мама дуже смачно підсмажує скибочки хліба, користуючись спеціальною маленькою сковорідкою.
Підсмаживши одну сторону кожної скибочки, вона перевертає її на іншу сторону.
Підсмажування кожної сторони скибочки триває 30 секунд, причому на сковорідці вміщується поруч тільки дві скибочки.
Зметикуйте, яким чином при цих умовах мама підсмажує обидві сторони трьох скибочок тільки за 1½ хвилини, а не за 2.
"""

BREAD_SIDES = 2
TIME_OVER = 1.5
FRYING_PAN_SIZE = 2
TIME_FRYING = 0.5

max_turns = TIME_OVER // TIME_FRYING
turns = 0
count_bread = 3
frying_bread = 0

breads = [[False for i in range(BREAD_SIDES)] for n in range(count_bread)]
pan = [[]]

def frying():
    global pan

    for bread in pan:
        bread[0] = True

def upend(bread:list):
    bread.reverse()
    return bread


def change_bread():
    pass


if __name__ == '__main__':
    while turns < max_turns:
        turns += 1
        

    print(turns)
    print(breads)