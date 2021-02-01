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

