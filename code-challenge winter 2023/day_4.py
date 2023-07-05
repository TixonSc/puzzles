#14.01
"""
Казковому гномові щоночі потрібна нова свіча, якою він світить собі у дорозі, бродячи по місту.
Він може зробити 1 нову свічу з 5 свічкових недогарків.
Якщо в нього набереться 25 недогарків, то на скільки ночей йому вистачить запасу нових свічок?
"""


candle = 0
piece_candle = 25
number_of_night = 0


def have():
    global candle   
    global piece_candle
    global number_of_night  
    print(f"Перед нічю {number_of_night + 1} є:\nсвічокок {candle}, недогарків {piece_candle}.")


def nigth():
    global candle   
    global piece_candle
    global number_of_night  
    if not candle:
        if craft_candle():
            return nigth()
        else: return False
    else:
        candle -= 1
        piece_candle += 1
        number_of_night += 1
        return True


def craft_candle():
    global candle   
    global piece_candle
    global number_of_night  
    if piece_candle < 5:
        return False
    else:
        piece_candle -= 5
        candle += 1
        print(f"Гном зробив нову свічку з 5 недогарків, залишилося {piece_candle} недогарків.")
        return True


if __name__ == '__main__':
    while nigth():
        print(f"\tНіч {number_of_night}!\nЗалишок свічок {candle}, недогарків {piece_candle}\n")