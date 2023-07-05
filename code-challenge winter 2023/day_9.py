#19.01
"""
Розділити 10 апельсинів порівну між 12-ма особами, при умові, що різати кожний апельсин можна не більш як на 3 рівні частини.
"""

def drob(a:int, b:int):
    if a > 1:
        d = gcd(a, b)
        a //= d
        b //= d
    return [a, b]


def d_sum(a:list, b:list):
    return drob(a[0] + b[0], a[1] + b[1])


def gcd(a:int, b:int):
    if b == 0: return a
    return gcd(b, a % b)


def d_mul(a:int, b:list):
    return [int(b[0] * a), b[1]]


def d_eq(a:list):
    return int(a[0] / a[1])

ORANGES = 12
PEOPLES = 10
MAX_SUB = 3

one_people_need = drob(PEOPLES, ORANGES)

print(one_people_need)

variants = [drob(1, x) for x in range(2, MAX_SUB + 1)]

print(variants)


def for_everyone():
    if one_people_need != d_sum(variants[0], variants[1]):
        return variants


if __name__ == '__main__':
    for v in for_everyone():
        slises = d_eq(d_mul(ORANGES, v))
        print(f"for {v} need {slises} acts")
