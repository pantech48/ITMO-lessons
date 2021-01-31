from string import ascii_lowercase
from string import ascii_uppercase

def encode(s, rotn):

    alph_orig_l = list(ascii_lowercase)
    alph_orig_u = list(ascii_uppercase)



    alph_l = list(ascii_lowercase)
    alph_u = list(ascii_uppercase)

    lst = list(s)

    for i in range(rotn):

	    alph_l.append(alph_l[0]) 
	    alph_l.pop(0)


    for i in range(rotn):

	    alph_u.append(alph_u[0]) 
	    alph_u.pop(0)


    for i in range(len(lst)):
	    if lst[i].isalpha():
		    if lst[i].isupper():
			    lst[i] = alph_u[alph_orig_u.index(lst[i])]
		    else:
			    lst[i] = alph_l[alph_orig_l.index(lst[i])]
    
    return ''.join(lst)

print(encode('0a!A1b"B2c#C3d$D4e%E5f&F6g\'G7h(H8i)I9j*J k+K l,L m-M n.N o/O p:P q;Q r<R s=S t>T u?U v@V w[W x\\X y]Y z^Z _ ` { | } ~ ', 1 ))