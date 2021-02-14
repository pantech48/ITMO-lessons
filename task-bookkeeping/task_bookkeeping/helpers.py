"""
Модуль содержит вспомогательные функции, 
для которых создавать отдельный модуль не рационально
"""

import datetime
import os
from textwrap import dedent

import appdirs
from prettytable import PrettyTable



__all__ = (
	'prompt', 'input_int', 'input_float',
	'input_datetime', 'input_date',
	'print_table', 'print_payment',
	)


def prompt(msg, default=None, type_cast=None):
	""" Запрашивает данные от пользователя и возвращает ввод. """
	while 1:
		value = input(f'{msg}: ')
	
		if not value:
			return default

		if type_cast is None:
			return value

		try:
			return type_cast(value)
		except ValueError as err:
			print(err)



def input_int(msg='Введите число', default=None):
	"""Запрашивает целое число  пользователя и возвращает ввод"""
	return prompt(msg, default, type_cast=int)


def input_float(msg='Введите число', default=None):
	"""Запрашивает дробное число  пользователя и возвращает ввод"""
	return prompt(msg, default, type_cast=float)

def input_datetime(msg='Введите дату и время', default=None, fmt='%Y-%m-%d %H:%M:%S'):
	"""Запрашивает дату и время  пользователя и возвращает ввод"""
	return prompt(msg, default, type_cast=lambda value: datetime.datetime.strptime(value, fmt))
	

def input_date(msg='Введите дату', default=None, fmt='%Y-%m-%d'):
	"""Запрашивает дату от пользователя и возвращает ввод"""
	return prompt(
		msg, 
		default, 
		type_cast=lambda value: datetime.datetime.strptime(value, fmt)
	)


def print_table(headers, iterable):
	"""Распечатывает таблицу на экран"""

	def datetime_convert_to_date(iterable):
		for obj in iterable:
			if isinstance(obj, datetime.datetime):
				iterable[iterable.index(obj)] = obj.date()

	table = PrettyTable(headers.values())
	for row in iterable:
		data = []

		for col_name in headers:
			data.append(row[col_name])

		datetime_convert_to_date(data)

		table.add_row(data)
	
	print(table)


def print_payment(payments):
	"""Распечатывает платёж на экран"""
	print(dedent(f'''
	***************************************************************
			    Платёж: "{payments['payment']}"
	         Стоимость: "{payments['price']}"
	        Количество: "{payments['amount']}"
	   Дата добавления: "{payments['created']:%d.%m.%Y}"
	***************************************************************
	'''))


def makedirs_if_not_exists(path):
	"""Создает все несуществующие директории в переданном пути."""
	if not os.path.exists(path):
		os.makedirs(path, 0o755) # mkdir -p path 
	return path


"""
Использовать с осторожностью!!!

__package__ == None, если модуль используется как исполняемый (главный)
__package__ == имя_пакета, если модуль используется как модуль.
"""
user_config_dir = makedirs_if_not_exists(
	appdirs.user_config_dir(__package__)
	) 
user_data_dir = makedirs_if_not_exists(
	appdirs.user_data_dir(__package__)
	) 
