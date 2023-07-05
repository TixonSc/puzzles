#24.01
"""
Знайти тризначні числа виду аbс, цифри яких задовольняють рівнянню a² – b² – с² = а – b – с (всі 3 цифри числа повинні бути різні).
"""
import math



numbers = list(range(1,10))

if __name__ == '__main__':
    result = []

    for a in numbers:

        for b in numbers:
            if b == a: continue

            for c in numbers:
                if c == b or c == a: continue

                A, B, C = {math.pow(a, 2), math.pow(b, 2), math.pow(c, 2)}
                left = int(A - B - C)
                rigth = a - b - c
                
                if left == rigth:
                    result.append([a,b,c])
                    print(f"{A} - {B} - {C} = {left} ? {rigth} = {a} - {b} - {c}")

    print(result)