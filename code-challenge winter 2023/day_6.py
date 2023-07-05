#16.01
"""
Кіт Мурко щойно «допомагав» своїй юній господині вирішувати завдання. Тепер він солодко спить, а уві сні бачить себе оточеним тринадцятьма (13) мишами.
Дванадцять мишей сірих, а одна — біла. І чує кіт, що каже хтось знайомим голосом:
«Мурко, ти повинен з'їдати кожну тринадцяту мишку, рахуючи їх по колу весь час в одному напрямку, з таким розрахунком, щоб останньою була з'їдена біла миша».
З якої мишки почати?
"""

GREY = False
WHITE = True
COUNT_OF_MOUSES = 13

mouses = [GREY for m in range(COUNT_OF_MOUSES - 1)]
mouses.append(WHITE)
count_mouses = len(mouses)
previus_mouse = 0

first_variants = [] #


def eat(mouses_l:list):
    global previus_mouse
    return mouses_l.pop(previus_mouse)


def next(mouses_l):
    global previus_mouse
    global count_mouses

    count_mouses = len(mouses_l)
    previus_mouse += COUNT_OF_MOUSES - 1

    while previus_mouse >= count_mouses and count_mouses:
        previus_mouse -= count_mouses
    
    return previus_mouse


if __name__ == '__main__':
    for variant in range(COUNT_OF_MOUSES):
        previus_mouse = variant
        l_mouses = [mouse for mouse in mouses]
        queue_mouse = []
        print(f"\n\nvariant {variant + 1}")

        while True:
            queue_mouse.append(eat(l_mouses))
            print(f"{len(queue_mouse)}`s EAT number {previus_mouse + 1} >>> " + ("White" if queue_mouse[-1] else "Grey"))
            if queue_mouse[-1]: break
            next(l_mouses)
        
        first_variants.append(queue_mouse)
        print(queue_mouse)
        if len(queue_mouse) == COUNT_OF_MOUSES and queue_mouse[-1]:
            print(f"\n\n---This is true answer!---\nvariant {variant + 1}\t{mouses}\n\n")

    print(first_variants)