import pytest

"""
unit my_tests
"""

def test_sum():
    """
    проверка сложения двух чисел
    :return:
    """
    assert (3 + 2) == 5


def test_len_of_string():
    """
    проверка количества букв в слове
    :return:
    """
    my_string = 'test'
    assert len(my_string) == 4


def test_concatenate_two_strings():
    """
    проверка сложения двух строк
    :return:
    """
    string1 = 'string1'
    string2 = 'string2'
    assert string1 + string2 == 'string1string2'


def test_len_of_list():
    """
    проверка создания списка нужной длины
    :return:
    """
    my_list = (1, 3, 5)

    assert len(my_list) == 3


def test_len_of_dict():
    """
    проверка длины словаря
    :return:
    """
    my_dict = {'1':'2', '3':'4'}
    assert len(my_dict) == 2


def test_len_of_string2():
    """
    проверка длины строки
    :return:
    """
    my_string = '1234567890'
    assert len(my_string) == 10


def test_devide_numbers():
    """
    проверка деления
    :return:
    """
    assert (9 // 3) == 3


def test_multiply_string():
    """
    умножение в строках
    :return:
    """
    my_string = 'otus'
    assert (my_string * 2) == 'otusotus'


def test_key_in_dict():
    """
    проверка ключа в словаре
    :return:
    """
    my_dict = {'1':'2', '3':'4'}
    assert my_dict['1'] == '2'


def test_len_of_set():
    """
    проверка длины множества
    :return:
    """
    my_set = (1, 2, 3, '45')
    assert len(my_set) == 4
