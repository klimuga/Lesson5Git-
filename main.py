import shutil
import use_functions
import victory
import sys
import os

def ActionPrint(printline, OutputTo="console"):
    """
    :param printline: what to print
    :return:
    """
    if OutputTo == "console":
        print(printline)
        return printline
    else:
        pass


def ActionInput(requestline, OutputTo="console"):
    if OutputTo == "console":
        InputData = input(requestline)
        return InputData
    else:
        pass

def Invitation(PreSelectedAction = 0, OutputTo="console"):
    if(PreSelectedAction == 0):
        ActionPrint("\nМеню:\n\n"
          "1  создать папку\n"
          "2  удалить (файл/папку)\n"
        "3  копировать (файл/папку)\n"
        "4  просмотр содержимого рабочей директории\n"
        "5  посмотреть только папки\n"
        "6  посмотреть только файлы\n"
        "7  просмотр информации об операционной системе\n"
        "8  создатель программы\n"
        "9  играть в викторину\n"
        "10 мой банковский счет\n"
        "11 смена рабочей директории (*необязательный пункт)\n"
        "12 выход.", OutputTo)
        SelectedAction = ActionInput("Введите ваш выбор: ", OutputTo)
        if SelectedAction.isdigit():
            SelectedAction = int(SelectedAction)
        else:
            ActionPrint("ОШИБКА. Введите число, другие вводы недопустимы.", OutputTo)
            SelectedAction = 0
        return SelectedAction
    else:
        SelectedAction = int(PreSelectedAction)
        ActionPrint("Функция Invitation получила параметры PreSelectedAction = {}, OutputTo = {}".format(PreSelectedAction, OutputTo), OutputTo)
        return SelectedAction

def ActionMkDir(): # 1 создать папку
    CreateDirName = ActionInput("Как назвать создаваемую папку? ")
    if not os.path.exists(CreateDirName):
        os.mkdir(CreateDirName)
        ActionPrint("УРА. папка {} успешно создана.".format(CreateDirName))
    else:
        ActionPrint("ОШИБКА. папка {} уже существует. Оставляю как есть.".format(CreateDirName))

def ActionRmFileDir(): # 2 удалить (файл/папку)
    RemoveDirName = ActionInput("Какую папку удалить? ")
    if os.path.exists(RemoveDirName):
        os.rmdir(RemoveDirName)
        ActionPrint("УРА. папка {} успешно удалена.".format(RemoveDirName))
    else:
        ActionPrint("ОШИБКА. папка {} не существует. Ничего не делаю.".format(RemoveDirName))

def ActionCopyFileDir(): # 3 копировать (файл/папку)
    CopyDirFileName = ActionInput("Какой файл или папку копировать? ")
    CopyDirFileNameDestination = ActionInput("Как назвать файл или папку? ")
    if os.path.exists(CopyDirFileNameDestination):
        ActionPrint("ОШИБКА. папка или файл {} уже существует.".format(CopyDirFileNameDestination))
        return False
    elif not os.path.exists(CopyDirFileName):
        ActionPrint("ОШИБКА. папка {} не существует. Ничего не делаю.".format(CopyDirFileName))
        return False
    else:
        if os.path.isfile(CopyDirFileName):
            shutil.copy(CopyDirFileName, CopyDirFileNameDestination)
        else:
            shutil.copytree(CopyDirFileName, CopyDirFileNameDestination)
        ActionPrint("УРА. Скопировал {} в {}".format(CopyDirFileName, CopyDirFileNameDestination))
        return True

def ActionLsDir(key=""): # 4 просмотр содержимого рабочей директории
    """
    :param key: "" - everything, "-d" - only dirs, no subdirs, "-f" - only files, no subdirs
    :return:
    """
    if key == "":
        ActionPrint("Содержимое текущей директории: ")
        for x in os.listdir():
            ActionPrint(x)
        ActionPrint("УРА. Удалось показать всё содержимое директории!!! ВАУ!!!")
    elif key == "-d":
        onlydirs = [f for f in os.listdir() if os.path.isdir(f)]
        ActionPrint("Содержимое текущей директории (только директории): ")
        for x in onlydirs:
            ActionPrint(x)
        ActionPrint("УРА. Удалось показать все директории!!! ВАУ!!!")
    elif key == "-f":
        onlyfiles = [f for f in os.listdir() if os.path.isfile(f)]
        ActionPrint("Содержимое текущей директории (только файлы): ")
        for x in onlyfiles:
            ActionPrint(x)
        ActionPrint("УРА. Удалось показать все файлы из директории!!! ВАУ!!!")
    else:
        ActionPrint("ОШИБКА, функции передан неверный ключ.")

def ActionChDir():
    ActionPrint("текущая директория: os.getcwd()={}".format(os.getcwd()))
    NewDir = ActionInput("Введите новую директорию: ")
    if NewDir.find("\\"):
#       ActionPrint("found \\")
        os.chdir(NewDir)
    else:
        os.chdir(os.getcwd() + "\\" + NewDir)
    ActionPrint("текущая директория: os.getcwd()={}".format(os.getcwd()))

if __name__ == "__main__":
    SelectedAction = Invitation()

    while SelectedAction != 12:
        if SelectedAction == 1: # создать папку
            ActionMkDir()
        elif SelectedAction == 2: # удалить (файл/папку)
            ActionRmFileDir()
        elif SelectedAction == 3: # копировать (файл/папку)
            ActionCopyFileDir()
        elif SelectedAction == 4: # просмотр содержимого рабочей директории
            ActionLsDir()
        elif SelectedAction == 5: # посмотреть только папки
            ActionLsDir("-d")
        elif SelectedAction == 6: # посмотреть только файлы
            ActionLsDir("-f")
        elif SelectedAction == 7: # просмотр информации об операционной системе
            ActionPrint("sys.version_info: ", sys.version_info)
        elif SelectedAction == 8: # создатель программы
            ActionPrint("Программу сию написал Гэндальф Белый, о мой юный подаван.")
        elif SelectedAction == 9: # играть в викторину
            victory.Victorina()
        elif SelectedAction == 10: # мой банковский счет
            use_functions.AccountManagement()
        elif SelectedAction == 11: # смена рабочей директории (*необязательный пункт)
            ActionChDir()
        elif SelectedAction == 12: # выход
            break
        else:
            ActionPrint("Ошибка, некорректный ввод.")
        SelectedAction = Invitation()
