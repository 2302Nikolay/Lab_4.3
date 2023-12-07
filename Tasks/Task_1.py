#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создать класс Triad (тройка чисел); определить метод сравнения триад (см. задание 2).
Определить производный класс Time с полями: час, минута и секунда. Определить полный
набор методов сравнения моментов времени
"""


class Triad:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def compare(self, other):
        # Сравниваем значения полей троек чисел
        if self.a == other.a and self.b == other.b and self.c == other.c:
            return "Триады равны"
        elif (
            self.a > other.a
            or (self.a == other.a and self.b > other.b)
            or (self.a == other.a and self.b == other.b and self.c > other.c)
        ):
            return "Первая триада больше второй"
        else:
            return "Вторая триада больше первой"


class Time(Triad):
    def __init__(self, hour, minute, second):
        super().__init__(hour, minute, second)

    def compare(self, other):
        # Сравниваем значения полей моментов времени
        if (
            self.a > other.a
            or (self.a == other.a and self.b > other.b)
            or (self.a == other.a and self.b == other.b and self.c > other.c)
        ):
            return "Первый момент времени больше второго"
        elif self.a == other.a and self.b == other.b and self.c == other.c:
            return "Моменты времени равны"
        else:
            return "Второй момент времени больше первого"


if __name__ == "__main__":
    # Создаем объекты класса Triad
    triad1 = Triad(1, 2, 3)
    triad2 = Triad(4, 5, 6)
    print(triad1.compare(triad2))  # Сравниваем тройки чисел

    # Создаем объекты класса Time
    time1 = Time(10, 20, 30)
    time2 = Time(10, 20, 30)
    print(time1.compare(time2))  # Сравниваем моменты времени
