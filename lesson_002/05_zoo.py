#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo_list = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo_list.insert(0, 'bear')
print(zoo_list)
# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

zoo_list.extend(['rooster','ostrich','lark'])
print(zoo_list)
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль

zoo_list.remove('elephant')
print(zoo_list)
# уберите слона
#  и выведите список на консоль

print(zoo_list.index("lion"))
print(zoo_list.index("lark"))
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.



