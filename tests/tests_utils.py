import pytest
from utils import get_data, get_last_values, get_filtered_data, get_formatted_data

def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x["date"] for x in data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364',
                                        '2019-04-04T23:20:05.206878', '2019-03-23T01:09:46.296404']

def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert [x["date"] for x in data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364',
                                        '2018-06-30T02:08:58.425572', '2018-03-23T10:45:06.972075',
                                        '2019-04-04T23:20:05.206878', '2019-03-23T01:09:46.296404']

def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['26.08.2019 Перевод организации\n'
                     ' Maestro 1596 93** **** 5199 -> ** 9589\n'
                     ' 31957.58 руб.\n',
                     '03.07.2019 Перевод организации\n'
                     ' MasterCard 7158 80** **** 6758 -> ** 5560\n'
                     ' 8221.37 USD\n',
                     '30.06.2018 Перевод организации\n'
                     ' Счет 75106830 21** **** 6952 -> ** 6702\n'
                     ' 9824.07 USD\n',
                     '23.03.2018 Открытие вклада\n  -> ** 2431\n 48223.05 руб.\n',
                     '04.04.2019 Перевод со счета на счет\n'
                     ' Счет 19708645 24** **** 8542 -> ** 4188\n'
                     ' 79114.93 USD\n',
                     '23.03.2019 Перевод со счета на счет\n'
                     ' Счет 44812258 98** **** 4719 -> ** 1160\n'
                     ' 43318.34 руб.\n']