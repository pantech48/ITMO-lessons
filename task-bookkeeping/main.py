from datetime import datetime
import sqlite3   

# with sqlite3.connect('schema.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES) as conn:

#     sql = '''
#     CREATE TABLE IF NOT EXISTS payment (
#         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#         title VARCHAR(100) NOT NULL,
#         price INTEGER NOT NULL,
#         amount INTEGER NOT NULL DEFAULT 1,
#         date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
#     )
#     '''

def display(type_cast=int):
   
    menu = """
1. Добавить платёж
2. Отредактировать платёж,
3. Вывести все платежи,
4. Вывести все платежи за указанный период,
5. Вывести топ самых крупный платежей,
6. Показать меню,
7. Закрыть программу
    """
    print(menu)

    value = input()

    if not value.isnumeric():
        return print('Введите число')

    if not value in func_dict:
        return print('Введите номер соответсвующий команде')

    return function_executor(value)
    
    
    

def add_payment():
    return print('Добавить платеж')

def edit_payment():
    return print('Отредактировать платеж')
    
def disp_payment_all():
    return print('Вывести все платежи')
    

def disp_payment_period():
    return print('Вывести все платежи за указанный период')
    

def top_payment():
    return print('Вывести топ самых крупный платежей')
   

def show_menu():
    return print('Показать меню')
    

def close():
    global i
    i = 0
    return print('Закрыть программу')

func_dict = {
    '1': add_payment,
    '2': edit_payment,
    '3': disp_payment_all,
    '4': disp_payment_period,
    '5': top_payment,
    '6': show_menu,
    '7': close,
}

def function_executor(val):
    for i in func_dict:
        if i == val:
            return func_dict.get(i)()

i = 1

while i:
    display()