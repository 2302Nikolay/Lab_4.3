#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Soldier:
    def __init__(self, number, team):
        self.number = number
        self.team = team

    def go_to_hero(self, hero):
        print(f"Солдат {self.number} идет за героем {hero.number}")


class Hero:
    def __init__(self, number):
        self.number = number
        self.level = 1

    def increase_level(self):
        self.level += 1


if __name__ == "__main__":
    hero1 = Hero(1)
    hero2 = Hero(2)

    soldiers_team1 = []
    soldiers_team2 = []

    for _ in range(10):
        number = random.randint(1, 100)
        team = random.choice([1, 2])
        soldier = Soldier(number, team)

        if soldier.team == 1:
            soldiers_team1.append(soldier)
        else:
            soldiers_team2.append(soldier)

    if len(soldiers_team1) > len(soldiers_team2):
        hero1.increase_level()
    else:
        hero2.increase_level()

    soldier_to_follow = random.choice(soldiers_team1)
    soldier_to_follow.go_to_hero(hero1)

    print(f"Идентификационный номер солдата: {soldier_to_follow.number}")
    print(f"Идентификационный номер героя: {hero1.number}")
