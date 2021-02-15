from datetime import datetime, time


SQL_ADD_NEW_PAYMENT = 'INSERT INTO payments (payment, price, amount, created) VALUES (?, ?, ?, ?)'

SQL_EDIT_PAYMENT_BY_ID = 'UPDATE payments SET payment=?, price=?, amount=?, created=? WHERE id=?'

SQL_SELECT_ALL_PAYMENTS = 'SELECT id, payment, price, amount, (price*amount) AS cost, created FROM payments'

SQL_SELECT_ALL_PAYMENTS_FOR_PERIOD = f'{SQL_SELECT_ALL_PAYMENTS} WHERE created BETWEEN ? AND ?'

SQL_SELECT_TOP_PAYMENTS = f'{SQL_SELECT_ALL_PAYMENTS} ORDER BY cost DESC LIMIT 4'

SQL_SELECT_TOP_PAYMENTS_BY_LIMIT = f'{SQL_SELECT_ALL_PAYMENTS} ORDER BY cost DESC LIMIT ?'

SQL_SELECT_PAYMENT_BY_ID = f'{SQL_SELECT_ALL_PAYMENTS} WHERE id=?'

SQL_DELETE_ALL_PAYMENTS = 'DELETE FROM payments'


def initialize(conn, creation_script):
    """Используя переданный SQL-скрипт, инициализирует структуру БД."""
    conn.executescript(creation_script)


def create_payment(conn, payment, price, created, amount=1):
    """Сохраняет новый платёж в БД."""
    conn.execute(SQL_ADD_NEW_PAYMENT, (payment, price, amount, created))


def edit_payment(conn, payment_id, payment, price, created, amount=1):
    """Редактирует платёж в БД"""
    created = datetime.combine(created, time())
    conn.execute(SQL_EDIT_PAYMENT_BY_ID, (payment, price, amount, created, payment_id))


def get_top_payments(conn, limit):
    """Возвращает задачи отсортированные по стоимости в заданном количестве"""
    return conn.execute(SQL_SELECT_TOP_PAYMENTS_BY_LIMIT, (limit,)).fetchall()


def get_payments_per_dates(conn, date_first, date_sec):
    """Возвращает задачи за указанный промежуток."""
    return conn.execute(SQL_SELECT_ALL_PAYMENTS_FOR_PERIOD, (date_first, date_sec)).fetchall() 


def get_all_payments(conn):
    """Возвращает все платежи из БД."""
    return conn.execute(SQL_SELECT_ALL_PAYMENTS).fetchall()


def get_payment(conn, payment_id):
    """Выбирает и возвращает из БД платёж с указанным первичным ключом."""
    return conn.execute(SQL_SELECT_PAYMENT_BY_ID, (payment_id,)).fetchone()


def delete_all_payments(conn):
    """Удаляет все платежи из таблицы"""
    conn.execute(SQL_DELETE_ALL_PAYMENTS)

