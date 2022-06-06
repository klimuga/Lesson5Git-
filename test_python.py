"""
1. В проекте создать новый модуль test_python.py

2. В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
Чем больше тестов на каждую функцию - тем лучше
"""

import math


def test_filter():

    assert list(filter(lambda x: x in (1,2,3), (1,3))) == [1,3]
    assert list(filter(lambda x: x in ["a","b","c","d","e","f"], ["a"])) == ["a"]

def test_pi():
    assert math.pi> 3 and math.pi < 4
    assert math.pi>3.14 and math.pi<3.15

def test_sqrt():
    assert math.sqrt(4)==2
    assert math.sqrt(9)==3

def test_pow():
    assert math.pow(2,2)==4
    assert math.pow(3,3)==27

def test_hypot():
    assert math.hypot(3,4)==5
    assert math.hypot(12,5)==13