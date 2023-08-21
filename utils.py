import json
from datetime import datetime

def load_file(data):
    """ функция получает данные из файла json"""
    with open(data, 'r', encoding='utf-8') as f:
        data_new = json.loads(f.read())
        return data_new

def sorting_from_empty(list_from_file):
    """ функция выборки выполненых операций"""
    list_from_file_new = []
    for i in list_from_file:
        if i.get('state') == 'EXECUTED':
            list_from_file_new.append(i)
    return list_from_file_new

def sorting_from_data(list_from_file):
    """сортировка по дате"""
    list_from_file.sort(key=lambda x: x['date'], reverse=True)
    return list_from_file


def datatime(text):
    """функция преобразования даты"""
    datetime_object = datetime.strptime(text, '%Y-%m-%dT%H:%M:%S.%f')
    return f"{datetime_object.day}.{datetime_object.month}.{datetime_object.year}"


def input_to(account_to):
    """функция вывода откуда идет перевод"""
    if "from" in account_to:
        new = account_to['from']
        len_s = len(new)
        if "Счет" in new:
            return new[0:len_s - 20] + '**' + new[-4:]
        else:
            return new[0:len_s - 12] + ' ' + new[len_s - 13:len_s - 11] + '** **** ' + new[-4:]
    else:
        return "Выполнен перевод на счет вклада"

def mask_account_number(account_number):
    """функция маскировки номера"""
    new = account_number["to"]
    len_s = len(new)
    if "Счет" in new:
        return new[0:len_s - 20] + '**' + new[-4:]
    else:
        return new[0:len_s - 12] + ' ' + new[len_s - 13:len_s - 11] + '** **** ' + new[-4:]

def print_to_sum(sorting_dict):
    """функция печати суммы операции и валюты"""
    return f'{sorting_dict["operationAmount"]["amount"]} {sorting_dict["operationAmount"]["currency"]["name"]}'

def print_from_to(sorting_dict):
    """функция печати откуда и куда идет перевод"""
    return f'{input_to(sorting_dict)} -> {mask_account_number(sorting_dict)}'

def print_date_description(sorting_dict):
    """функция печати  даты и описания операции"""
    return f'{datatime(sorting_dict["date"])} {sorting_dict["description"]}'
