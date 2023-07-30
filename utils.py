from datetime import datetime, date
import json

def get_data():
    """Функция возвращает список транзакций из JSON"""
    with open('operations.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data

def get_filtered_data(data):
    """Функция фильтрует список по параметру EXECUTED"""
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data

def get_last_values(data, count_last_values):
    """Функция сортирует список от самой последней операции. Выводит заданное количество операций"""
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:count_last_values]
    return data

def get_formatted_data(data):
    """Функция формирует нужные сообщения для вывода"""
    formatted_date = []
    for row in data:
        normalized_date = date.fromisoformat(row["date"][:10])
        operation_date = normalized_date.strftime('%d.%m.%Y')
        operation_description = row['description']
        if 'from' in row:
            open_from = (f'{row["from"][:-12]} {row["from"][:-12:-10]}** **** {row["from"][-4:]}')
        else:
            open_from = ''
        operation_from = open_from
        open_to = row["to"]
        operation_to = (f'** {open_to[-4:]}')
        operation_amount = row['operationAmount']['amount']
        operation_currency = row['operationAmount']['currency']['name']
        formatted_date.append(f'{operation_date} {operation_description}\n {operation_from} -> {operation_to}\n '
                              f'{operation_amount} {operation_currency}\n')

    return formatted_date
