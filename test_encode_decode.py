# s = '0a!A1b"B2c#C3d$D4e%E5f&F6g\'G7h(H8i)I9j*J k+K l,L m-M n.N o/O p:P q;Q r<R s=S t>T u?U v@V w[W x\\X y]Y z^Z _ ` { | } ~ '

# rotn = 1

# #   '0b!B1c"C2d#D3e$E4f%F5g&G6h\'H7i(I8j)J9k*K l+L m,M n-N o.O p/P q:Q r;R s<S t=T u>U v?V w@W x[X y\\Y z]Z a^A _ ` { | } ~ '

# def encode(s, rotn):
# 	text = list(s)
# 	text_filt = list(filter(lambda x: x.isalpha(), text))

	

# encode('0a!A1b"B2c#C3d$D4e%E5f&F6g\'G7h(H8i)I9j*J k+K l,L m-M n.N o/O p:P q;Q r<R s=S t>T u?U v@V w[W x\\X y]Y z^Z _ ` { | } ~ '
# , 0)

# import string

# alph_orig_l = list(string.ascii_lowercase)
# alph_orig_u = list(string.ascii_uppercase)



# alph_l = list(string.ascii_lowercase)
# alph_u = list(string.ascii_uppercase)


# code = 1

# '''for i in range(len(alph)):
	
# 	if (i + code) > len(alph):
# 		i = 0
# 		alph[i] = alph[i+code]
# 		print(alph[i])
# 	else:
# 		alph[i] = alph[i+code]
# 		print(alph[i])
# print(alph)'''

# i = 0

# '''while i <= len(alph):

# 	if (i + code) >= len(alph):
# 		i = 0
# 		alph[i] = alph[i+code]
# 		print(alph[i])
# 	else:
# 		alph[i] = alph[i+code]
# 		print(alph[i])
# 	i += 1	'''




# lst = list(s)

# code = 2


# for i in range(code):

# 	alph_l.append(alph_l[0]) 
# 	alph_l.pop(0)


# for i in range(code):

# 	alph_u.append(alph_u[0]) 
# 	alph_u.pop(0)


# for i in range(len(lst)):
# 	if lst[i].isalpha():
# 		if lst[i].isupper():
# 			lst[i] = alph_u[alph_orig_u.index(lst[i])]
# 		else:
# 			lst[i] = alph_l[alph_orig_l.index(lst[i])]
		
		
# print(lst)

from string import ascii_lowercase
from string import ascii_uppercase


def decode(s, rotn):

    alph_orig_l = list(ascii_lowercase)
    alph_orig_u = list(ascii_uppercase)



    alph_l = list(ascii_lowercase)
    alph_u = list(ascii_uppercase)

    lst = list(s)

    for i in range(rotn):

	    alph_l.insert(0, alph_l.pop()) 

	  


    for i in range(rotn):

	    alph_u.insert(0, alph_u.pop()) 
	

    for i in range(len(lst)):
	    if lst[i].isalpha():
		    if lst[i].isupper():
			    lst[i] = alph_u[alph_orig_u.index(lst[i])]
		    else:
			    lst[i] = alph_l[alph_orig_l.index(lst[i])]
    
    return ''.join(lst)

print(decode('0c!C1d"D2e#E3f$F4g%G5h&H6i\'I7j(J8k)K9l*L m+M n,N o-O p.P q/Q r:R s;S t<T u=U v>V w?W x@X y[Y z\\Z a]A b^B _ ` { | } ~ ', 2))