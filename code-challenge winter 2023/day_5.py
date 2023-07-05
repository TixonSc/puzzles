#15.01
"""
В Америці дату 1 липня 2003 року записують так: 7/1/2003, а в інших країнах: 1/7/2003.
Якщо не знати, у якому форматі записане число, то скільки дат у році можна витлумачити невірно?
"""

YEAR = 2022
DAYS_IN_MONTH = 30
MONTH_IN_YEAR = 12

format_other_world = "{d}/{m}/{y}"
format_american = "{m}/{d}/{y}"

list_of_false = []
format_for_list = "{usa} vs {www}"


if __name__ == '__main__':
    dates_world = [[format_other_world.format(d=day, m=month, y=YEAR) for day in range(1, DAYS_IN_MONTH + 1)] for month in range(1, MONTH_IN_YEAR + 1) ]
    dates_usa = [[format_american.format(d=day, m=month, y=YEAR) for day in range(1, DAYS_IN_MONTH + 1)] for month in range(1, MONTH_IN_YEAR + 1) ]

    for month in dates_world:
        for day in month:

            for m in dates_usa:
                for d in m:
                    if day == d:
                        list_of_false.append(format_for_list.format(usa=day, www=day))
                        print(list_of_false[-1])

    print(f"\ncount of shit dates {len(list_of_false)}\n")
    print(list_of_false)