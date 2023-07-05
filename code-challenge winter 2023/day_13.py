#23.01
"""
Два товарних поїзди, обидва довжиною у 250 м, їдуть назустріч один одному з однаковою швидкістю 45 км/год.
Скільки секунд пройде після того, як зустрілися машиністи, перш ніж зустрінуться кондуктори останніх вагонів?
"""

speed = 45 #on hour
length = 250 #metrs


def m_sec(speed):
    secs = 3600
    metr_in_km = 1000

    return (speed * metr_in_km) / secs


if __name__ == '__main__':
    m_speed = m_sec(speed)
    time = length / m_speed #x2 len // y2 speed
    print(f"by speed:{speed} km/h, length:{length} m\nsec_speed:{m_speed}m/s, time:{time} sec")