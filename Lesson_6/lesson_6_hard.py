
__author__ = 'Ильясов Исмаил Ильясович'

#HARD

# Задание-1:
#
# Написать класс, который будет удобно использовать для работы с (на выбор что-нибудь одно) комплексными числами \ матрицами \ светофор \ микроволновка
# Чем логичнее код тем лучше

import math

class complex_numbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'complex_numbers({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return complex_numbers(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return complex_numbers(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return complex_numbers(-self.x, -self.y)

x = complex_numbers(5, 8)
y = complex_numbers(3, 5)
z = complex_numbers('drt', 'hfj')
w = complex_numbers('www', 'ukj')
print(x + y)
print(x - y)
print(z + w)
# print(x + 1)
print(x.__iadd__(y))


# Задание-2: не обязательно
#
# Написать консольную РПГ игру...
# Пример:

# <Характеристики персонажа>   <Характеристики врага>
# (HP, MP, Power, Defense)
#
# <Выбор действий>
# (Атаковать, Лечиться, .....)