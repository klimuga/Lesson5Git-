"""
3. В том же проекте создать модуль test_main.py для
тестирования функций консольного файлового менеджера
4. В файле написать тесты для каждой "чистой" функции,
чем больше тем лучше. Это могут быть функции консольного
файлового менеджера, а так же программы мой счет и программы викторина
5. (Дополнительно*) так же попробовать написать тесты
для ""грязных"" функций, например копирования файла/папки, ...
8. Создать pull request на объединение веток master и
новой ветки с тестами, прислать ссылку на pull request как решение дз
"""
#from main import ActionPrint
from main import *
#import math

def test_ActionPrint():
    printline ="abcd"
    assert printline == ActionPrint(printline)

def test_ActionPrint1():
    printline = "abcd"
    assert printline == ActionPrint(printline, "console")

def test_Invitation():
    for i in range(1, 13):
        InvitationOutput = Invitation(i, "console")
        assert InvitationOutput == i

