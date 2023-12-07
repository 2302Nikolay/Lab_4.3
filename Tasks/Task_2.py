#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создать абстрактный базовый класс Pair с виртуальными арифметическими операциями.
Создать производные классы Money (деньги) и Fraction (дробное число).
"""


from abc import ABC, abstractmethod


# Создаем абстрактный класс Pair
class Pair(ABC):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __truediv__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Создаем класс Money, который наследуется от Pair
class Money(Pair):
    def __init__(self, amount):
        self.amount = amount

    # Переопределяем методы сложения, вычитания, умножения, деления и вывода для класса Money
    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(self.amount - other.amount)
        else:
            raise TypeError("Unsupported operand type")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other)
        else:
            raise TypeError("Unsupported operand type")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount / other)
        else:
            raise TypeError("Unsupported operand type")

    def __str__(self):
        return str(self.amount)


# Создаем класс Fraction, который наследуется от Pair
class Fraction(Pair):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # Переопределяем методы сложения, вычитания, умножения, деления и вывода для класса Fraction
    def __add__(self, other):
        if isinstance(other, Fraction):
            common_denominator = self.denominator * other.denominator
            new_numerator = (self.numerator * other.denominator) + (
                other.numerator * self.denominator
            )
            return Fraction(new_numerator, common_denominator)
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            common_denominator = self.denominator * other.denominator
            new_numerator = (self.numerator * other.denominator) - (
                other.numerator * self.denominator
            )
            return Fraction(new_numerator, common_denominator)
        else:
            raise TypeError("Unsupported operand type")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Fraction(self.numerator * other, self.denominator)
        else:
            raise TypeError("Unsupported operand type")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Fraction(self.numerator, self.denominator * other)
        else:
            raise TypeError("Unsupported operand type")

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


# Основной код программы
if __name__ == "__main__":
    money1 = Money(100)
    money2 = Money(50)
    print(money1 + money2)
    print(money1 - money2)
    print(money1 * 2)
    print(money1 / 2)
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(3, 4)
    print(fraction1 + fraction2)
    print(fraction1 - fraction2)
    print(fraction1 * 2)
    print(fraction1 / 2)
