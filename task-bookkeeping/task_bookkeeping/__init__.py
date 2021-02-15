from datetime import date, datetime, timedelta, time
import importlib.resources 
import sys

from task_bookkeeping import storage
from task_bookkeeping.helpers import (
    prompt, input_int, input_float, input_date, input_datetime,
    print_table, print_payment
)
from task_bookkeeping.services import make_db_connection


def input_payment():
    """Запрашивает идентификатор платежа и возвращает его из БД."""
    def cb(payment_id):
        with make_db_connection() as conn:
            payment = storage.get_payment(conn, int(payment_id))
            
            if payment is None:
                raise ValueError(f'Платёж с ID {payment_id} не найден.')
            
            return payment
    
    return prompt('Введите ID платежа', type_cast=cb)


def input_payment_data(payment=None):
    """Запрашивает данные от пользователя о платеже и возвращает ввод."""
    
    payment = dict(payment) if payment else {}
    today_dt = datetime.today()
    data = {}
    
    data['payment'] = prompt('Название', default=payment.get('payment', ''))
    
    
    data['price'] = input_float('Цена', default=payment.get('price', ''))

    data['amount'] = input_int('Количество', default=payment.get('amount', ''))
    
    data['created'] = input_date(
        'Дата',
        default=payment.get('created', datetime.combine(today_dt, time()))
    )
    return data


def menu_add_payment(): 
    """Добавить платёж"""
    with make_db_connection() as conn:
        data = input_payment_data()
        storage.create_payment(conn, **data)
        print(f'Платёж "{data["payment"]}" успешно создан.')


def menu_edit_payment(): 
    """Отредактировать платёж"""
    payment = input_payment()
    
    if payment is not None:
        with make_db_connection() as conn:
            data = input_payment_data(payment)
            storage.edit_payment(conn, payment['id'], **data)
            print(f'Платёж "{data["payment"]}" успешно отредактирован.')


def menu_show_all_payments(): 
    """Вывести весь список платежей"""
    
    with make_db_connection() as conn:
        payments = storage.get_all_payments(conn)
        print_table(
            {
                'id': 'ID',
                'payment': 'Название платежа',
                'cost': 'Стоимость',
                'created': 'Дата',
            },
            payments
        )



def menu_show_payments_for_period():
    """Показать платежи за период."""
    first_date = input_date('Введите начальный период')
    second_date = input_date('Введите конечный перид')

    with make_db_connection() as conn:
        payments = storage.get_payments_per_dates(conn, first_date, second_date)
        print_table(
            {
                'id': 'ID',
                'payment': 'Название платежа',
                'price': 'Цена',
                'amount': 'Количество',
                'cost': 'Стоимость'
            },
            payments
        )


def menu_show_top_payments():
    """Показать топ крупных платежей."""
    lim = input_int('Введите количество платежей', default=1)

    with make_db_connection() as conn:
        payments = storage.get_top_payments(conn, lim)
        print_table(
                {
                    'id': 'ID',
                    'payment': 'Наименование платежа',
                    'price': 'Цена',
                    'amount': 'Количество',
                    'cost': 'Стоимость'
                },
                payments
            )



def menu_delete_all_payments():
    """Удалить все платежи"""
    agreement = ('y', 'Y', 'Yes', 'yes')
    question = prompt('Вы действительно хотите удалить все платежи? [Y/N]')

    if question in agreement:
        with make_db_connection() as conn:
            storage.delete_all_payments(conn)
            print('Все платежи успешно удалены.')


def menu_show_menu():
    """Показать меню"""
    for cmd, action_tuple in actions.items():
        print(f'{cmd}. {action_tuple[1]}')


def show_usage():
    """Показать, как использовать"""
    commands = ', '.join(actions.keys())
    print(f'\nНеизвестная команда.\nВведите одну из: {commands}')


actions = {
    '1': (menu_add_payment, 'Добавить платёж'),
    '2': (menu_edit_payment, 'Отредактировать платёж'),
    '3': (menu_show_all_payments, 'Вывести все платежи'),
    '4': (menu_show_payments_for_period, 'Вывести все платежи за указанный период'),
    '5': (menu_show_top_payments, 'Вывести топ самых крупных платежей'),
    '6': (menu_delete_all_payments, 'Удалить все платежи'),
    'm': (menu_show_menu, 'Показать меню'),
    'q': (sys.exit, 'Выйти'),
}


def main():
    with make_db_connection() as conn:
        creation_script = importlib.resources.read_text('task_bookkeeping.resources', 'schema.sql')
        storage.initialize(conn, creation_script)
        
    
    menu_show_menu()
    
    while 1:
        cmd = input('\nВведите команду: ').strip()
        
        action_tuple = actions.get(cmd, (show_usage, ''))
        action_tuple[0]()