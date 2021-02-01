

'''
# из snake в camel
v = 'kgsy_x_brurjf_jh_mpxlmn'
a = v.split('_') #убираем "_" и делаем список слов
b = ' '.join(a)
s = b.title()
print(s)

filt_1 = tuple(filter(lambda x: x != " ", s))



print(''.join(filt_1))
'''


# из camel в snake



'''
camel = 'KgsyXBrurjfJhMpxlmn'
cam_lst = list(camel)
print(cam_lst)


def cam_decor(lst):
	i = 0

	while i < len(lst):

		if lst[i].isupper() == True:
			lst.insert(i, '_')
			i += 1
		i += 1


z = list(map(lambda x: x.insert(x, '_') if x.isupper(), cam_lst))
z.remove(cam_lst[0])
print(z)

str_snake = ''.join(z)
print(str_snake.lower())'''

'''
camel = 'KgsyXBrurjfJhMpxlmn'
cam_lst = list(camel)

def cam_decor(n):
	if n.isupper():
		s = '_' + n
		return 


z = list(map(cam_decor(n), cam_lst))

print(z)'''

'''def snake_to_camel(name):

	cam_lst = name.split('_') # Выводим список слов без '_'

	cam_str1 = ' '.join(cam_lst) # Вывод слитной строки

	cam_upc = cam_str1.title() 

	cam_filt = tuple(filter(lambda x: x != " ", cam_upc)) # Убираем пробелы

	return ''.join(cam_filt) 

print(snake_to_camel('kgsy_x_brurjf_jh_mpxlmn'))'''

'''def camel_to_snake(name):

	snk_lst = list(name)

	def decor(n):
		if n.isupper():
			n2 = '_' + n
			return n2



	snk_lst2 = list(map(decor, snk_lst))

	snk_lst2.remove(snk_lst2[0])

	return (''.join(snk_lst2)).lower()

print(camel_to_snake('KgsyXBrurjfJhMpxlmn'))'''


def camel_to_snake(name):

	snk_lst = list(name)

	def decor(n):
		if n.isupper():
			n2 = '_' + n
			return n2
		return n


	snk_lst_upd = list(map(decor, snk_lst))
	
	snk_lst_upd_2 = ''.join(snk_lst_upd).lower()

	return snk_lst_upd_2[1:]

print(camel_to_snake('KgsyXBrurjfJhMpxlmn'))