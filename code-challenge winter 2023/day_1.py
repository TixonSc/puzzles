#11.01 nomber 1
# Задача про бармена и интровертов

import math

NUMBBER_OF_CHAIRS = 25

class Bar:
    def __init__(self, first):
        self.chairs = [False for i in range(NUMBBER_OF_CHAIRS)]
        self.attractions = [0 for i in self.chairs]
        self.sequence = []
        self.sit_here(first)
        self.attraction()


    def count_of_introvert(self):
        return self.chairs.count(True)


    def __str__(self):
        return str(self.chairs) + "\n" + str(self.attractions) + "\n" + str(self.sequence)
        
    
    def sit_here(self, index):
        self.chairs[index] = True
        self.sequence.append(index + 1)

    def len_to_rigth(self, index):
        if index == (NUMBBER_OF_CHAIRS - 1): return NUMBBER_OF_CHAIRS
        len_r = 0

        while True:
            index += 1
            if self.chairs[index]: return len_r
            else: len_r += 1
            if index == (NUMBBER_OF_CHAIRS - 1): return len_r
                


    def len_to_left(self, index):
        if index == 0: return NUMBBER_OF_CHAIRS
        len_r = 0

        while True:
            index -= 1
            if self.chairs[index]: return len_r
            else: len_r += 1
            if index == 0: return len_r
            

    def attraction(self):
        index = -1
        for chair in self.chairs:
            index += 1

            if chair: 
                self.attractions[index] = -1
                continue
            else:
                left = self.len_to_left(index)
                right = self.len_to_rigth(index)
                if left == 0: right = 0
                if right == 0: left = 0
                self.attractions[index] = left * right
        return int(max(self.attractions))


    def introvert_incoming(self):
        max_attr = self.attraction()
        #print(self)
        if max_attr <= 0: return False
        else: 
            self.sit_here(self.attractions.index(max_attr))
            return True


result_by_first_introver_index = [Bar(n) for n in range(NUMBBER_OF_CHAIRS)]


if __name__ == '__main__':
    for every_first in result_by_first_introver_index:
        while every_first.introvert_incoming():
            continue
        index = result_by_first_introver_index.index(every_first)
        print(f"in Bar with first\t#{index + 1}\tthere are\t{every_first.count_of_introvert()}\tintroverts")
        print(f"{every_first}\n")