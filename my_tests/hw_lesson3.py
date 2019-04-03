"""
1. Тестирование REST сервиса 1
Написать автоматизированные тесты для REST API сервиса: https://dog.ceo/dog-api/. Документация к API есть на сайте.
Тесты должны быть параметризованными на уровне фикстур или самих тестов.
Критерии оценки:
Полнота тестового покрытия и качество кода. Код должен так же проходить проверки синтаксическим анализатором pylint.

2. Тестирование REST сервиса 2
Написать автоматизированные тесты для REST API сервиса: https://www.openbrewerydb.org/. Документация к API есть на сайте.
Тесты должны быть параметризованными на уровне фикстур или самих тестов. Тесты должны успешно проходить.
Критерии оценки:
Полнота тестового покрытия и качество кода. Код должен так же проходить проверки синтаксическим анализатором pylint.

3. Тестирование REST сервиса 3.
Написать автоматизированные тесты для REST API сервиса: https://cdnjs.com/api. Документация к API есть на сайте.
Тесты должны быть параметризованными на уровне фикстур или самих тестов. Тесты должны успешно проходить.
Критерии оценки:
Полнота тестового покрытия и качество кода. Код должен так же проходить проверки синтаксическим анализатором pylint.

4. Опции командной строки pytest
Добавить опции командной строки для запуска тестов. Опции командной строки должны позволять выбрать один из URL,
который тестируем или все, если выбран неподдерживаемый URL, то запуск тестов не должен происходить, должна быть выдана
ошибка на экран.

5. Скрипт для запуска тестов через argparse (Опционально)
Тоже самое, что и задание 3, но реализовать с помощью библиотеки argparse.

В качестве результата домашнего задания необходимо прислать ссылку на коммит в вашем github репозитории и вывод работы pylint.
"""

import pytest
import requests

API_ENDPOINTS = ['https://dog.ceo/api/breeds/list/all',
                 'https://dog.ceo/api/breeds/image/random',
                 'https://dog.ceo/api/breed/hound/images',
                 'https://dog.ceo/api/breed/hound/list']

HEADERS_LIST = [{"Content-type": "application/json"}, {"Content-type": "text/html"}]

BREEDS_LIST = ['affenpinscher', 'african', 'akita', 'boxer', 'bulldog']


@pytest.mark.run(order=2)
@pytest.mark.parametrize('endpoints', API_ENDPOINTS)
def test_by_endpoints(endpoints):
    """
    test_by_endpoints
    :param endpoints:
    :return:
    """
    resp = requests.get(endpoints)
    assert resp.status_code == 200


@pytest.mark.run(order=1)
@pytest.mark.parametrize('breeds', BREEDS_LIST)
def test_by_breeds(breeds):
    """
    test_by_breeds
    :param breeds:
    :return:
    """
    url = 'https://dog.ceo/api/breed/' + breeds + '/images/random'
    resp = requests.get(url)
    assert resp.status_code == 200


@pytest.mark.parametrize('headers', HEADERS_LIST)
def test_by_headers(headers):
    """
    test_by_headers
    :param headers:
    :return:
    """
    resp = requests.get('https://dog.ceo/api/breeds/image/random')
    assert resp.headers['Content-type'] == headers['Content-type']


@pytest.mark.parametrize('encoding', ['ascii', 'koi8-r', 'utf-8'])
def test_by_encoding(encoding):
    """
    test_by_encoding
    :param encoding:
    :return:
    """
    resp = requests.get('https://dog.ceo/api/breeds/image/random')
    assert resp.apparent_encoding == encoding


#  https://www.openbrewerydb.org/

base_url = 'https://api.openbrewerydb.org/breweries'

types_of_sorts = ['by_state', 'by_name', 'by_tag']
pagination = ['page=2', 'per_page=10']


@pytest.mark.parametrize('sort', types_of_sorts)
@pytest.mark.parametrize('page', pagination)
def test_by_types_sort_and_pagination(sort, page):
    resp = requests.get(base_url + '?' + sort + '?' + page)
    assert resp.status_code == 200


@pytest.mark.parametrize('nums', [x for x in range(10)])
def test_pagination2(nums):
    url = base_url + '?page={}'.format(nums)
    resp = requests.get(url)
    assert resp.status_code == 200


@pytest.mark.parametrize('per_page', [0, 1, 25, 49, 50, 51])
def test_pagination3(per_page):
    url = base_url + '?per_page={}'.format(per_page)
    resp = requests.get(url)
    assert resp.status_code == 200


#  https://cdnjs.com/api

