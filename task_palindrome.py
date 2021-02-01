'''
Напишите функцию is_palindrome(s), которая проверяет, является ли переданное число или строка палиндромом и возвращает True. В противном случае возвращает False.

Палиндром - это число или текст, который читается одинаково и слева, и справа, пробелы, знаки пунктуации и регистр символов не учитываются.

Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.
'''

def is_palindrome(s):
	if type(s) is str:

		low_s = list(s.lower())

		filt_s = tuple(filter(lambda x: x.isalnum(), low_s))
	
	else:

		filt_s = tuple(filter(lambda x: x.isalnum(), list(str(s))))
	

	if filt_s[::] == filt_s[::-1]:
		
		return 1 == 1
	
	else:
		return 1 != 1

print(is_palindrome('!a"a#a$a%a&a\'a(a)a*a+a,a-a.a/a:a;aa?a@a[a\\a]a^a_a`a{a|a}a~'))