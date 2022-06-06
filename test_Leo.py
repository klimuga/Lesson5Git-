from LEOvictory import *
from LEOmain import *
from LEOfilemanager import *
from LEObill import *

def test_date_to_str():
    assert date_to_str("01.01.1999") == "первое января 1999 года"
    assert date_to_str("26.02.1990") == "двадцать шестое февраля 1990 года"

def test_is_correct_choice():
    assert is_correct_choice("2") == True

def test_copy_file_or_directory():
    WeirdFileName1 = "sfdjkhOYUIO9879.py"
    WeirdFileName2 = "sfdjkhOYUIO98792.py"
    WeirdDirName1 =  "sfdjkhOYUIO98793"
    WeirdDirName2 =  "sfdjkhOYUIO98794"
    if not os.path.exists(WeirdFileName1) and not os.path.exists(WeirdFileName2):
        f1 = open(WeirdFileName1, "w")
        f1.write("hello")
        f1.close()
        copy_file_or_directory(WeirdFileName1, WeirdFileName2)
        assert os.path.exists(WeirdFileName2) == True
        os.remove(WeirdFileName1)
        os.remove(WeirdFileName2)
    if not os.path.exists(WeirdDirName1) and not os.path.exists(WeirdDirName2):
        os.mkdir(WeirdDirName1)
        copy_file_or_directory(WeirdDirName1, WeirdDirName2)
        assert os.path.exists(WeirdDirName2) == True
        os.rmdir(WeirdDirName1)
        os.rmdir(WeirdDirName2)
