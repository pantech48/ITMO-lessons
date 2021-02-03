
'''Файл data.txt заполнен случайными целыми числами, числа разделены одним пробелом.

Сформировать файл out-1.txt из элементов файла data.txt, делящихся без остатка на n. Если таких чисел нет, то создать пустой файл.
Сформировать файл out-2.txt из элементов файла data.txt, возведенных в степень p.
n и p - целые числа, вводимые с клавиатуры. В исходном файле может быть добавлен перенос строки в конце файла, не забудьте обработать этот случай.
'''
n = int(input()) # делим на n
p = int(input()) # возводим в степень p

with open('data.txt') as f:
    lines = f.read()
    strip_lines = lines.strip('\n ')
    lst_1 = strip_lines.split(' ')
    

a = list(filter(lambda x: int(x)%n == 0, lst_1))
b = list(map(lambda x: str(int(x)**p), lst_1))

print(b)

with open('out-1.txt', 'w') as f:
    if not a:
        f.write('')
    else:
        f.write(' '.join(a))

with open('out-2.txt', 'w') as f:
    f.write(' '.join(b))
