'''Реализуйте модуль для перевода числа из одной системы счисления в другую.

Модуль должен содержать 6 функций для перевода из десятичной системы счисления в двоичную, восьмеричную, шестнадцатиричную и наоборот:

dec2bin(number) # возвращает str
dec2oct(number) # возвращает str
dec2hex(number) # возвращает str
bin2dec(number) # возвращает int
oct2dec(number) # возвращает int
hex2dec(number) # возвращает int
(!) Запрещено использовать встроенные функции/методы, решающие эту задачу.

Подсказка. Не спешите писать 6 разных реализаций, подумайте, можно ли написать универсальный алгоритм перевода.

В решении не должно присутствовать операций ввода-вывода.

Ситуации, когда в исходном числе есть не допустимые цифры (буквы), игнорируются.

'''

def dec2ns(number, radix):
    oct = {
        'f': 15,
        'e': 14,
        'd': 13,
        'c': 12,
        'b': 11,
        'a': 10
    }
    

    num = []

    while number > radix:
        
        a = number % radix
        num.append(str(a))
        number = number // radix

        
    num.append(str(number))

    num.reverse()
    
    return int(''.join(num))


def ns2dec(number, radix):
    oct = {
        'f': 15,
        'e': 14,
        'd': 13,
        'c': 12,
        'b': 11,
        'a': 10
    }
    
   

    num = []
    n_lst = list(str(number))
    summ = 0

    if radix == 16:
        for i in range(len(n_lst)):
            if n_lst[i] in oct:
                n_lst[i] = oct.get(n_lst[i])

    for i in range(len(n_lst)):

        summ += int(n_lst[i])* (radix**((list(range(len(n_lst)))[::-1]))[i])
    return summ
