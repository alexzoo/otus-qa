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


@pytest.mark.parametrize('endpoints', API_ENDPOINTS)
def test_by_endpoints(endpoints):
    """
    test_by_endpoints
    :param endpoints:
    :return:
    """
    resp = requests.get(endpoints)
    assert resp.status_code == 200


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


