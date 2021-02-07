from datetime import datetime
import sqlite3   

with sqlite3.connect('schema.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES) as conn:

    sql = '''
    CREATE TABLE IF NOT EXISTS payment (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        title VARCHAR(100) NOT NULL,
        price INTEGER NOT NULL,
        amount INTEGER NOT NULL DEFAULT 1,
        date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    '''

def promt(type_cast=int):
   
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

    if not type_cast(value) in list(range(1, len(func_lst))):
        return print('Введите номер соответсвующий команде')

    return func_lst[type_cast(value)]()
    
    
    

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

a_p = add_payment
e_p = edit_payment
d_p_a = disp_payment_all
d_p_p = disp_payment_period
t_p = top_payment
s_m = show_menu
c = close
func_lst = [None, a_p, e_p, d_p_a, d_p_p, t_p, s_m, c]

i = 1

while i:
    promt()