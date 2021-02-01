


from datetime import date
from datetime import datetime
from datetime import time


def counter():
    
    today = datetime.now()

    new_year = datetime(today.year + 1, 1, 1, 0, 0)

    diff = abs(new_year - today) 

    d = diff.days
    h = diff.seconds//3600
    m = int(diff.seconds%3600)/60

    print(int(str(tuple(str(d))[-2]) + str(tuple(str(d))[-1])))
    print(h)
    print(int(m))
    

   
    if 2 <= int(tuple(str(int(d)))[-1]) <= 4:
        d_new = str(d) + ' дня '
    elif int(tuple(str(int(d)))[-1]) == 1:
        d_new = str(d) + ' день '
    else:
        d_new = str(d) + ' дней '

    if len(tuple(str(d))) > 1:
        if 11 <= int(str(tuple(str(d))[-2]) + str(tuple(str(d))[-1])) <= 19:
            d_new = str(d) + ' дней '



    

    if int(tuple(str(int(h)))[-1]) == 1:
        h_new = str(h) + ' час '
    elif 2 <= int(tuple(str(int(h)))[-1]) <= 4:
        h_new = str(h) + ' часа '
    else:
        h_new = str(h) + ' часов '
    
    if len(tuple(str(h))) > 1:
        if 11 <= int(str(tuple(str(h))[-2]) + str(tuple(str(h))[-1])) <= 19:
            h_new = str(h) + ' часов '



    
    if int(tuple(str(int(m)))[-1]) == 1: 	
        m_new = str(int(m)) + ' минута'
    elif 2 <= int(tuple(str(int(m)))[-1]) <= 4:
        m_new = str(int(m)) + ' минуты'
    else:
        m_new = str(int(m)) + ' минут'
    
    if len(tuple(str(int(m)))) > 1:

        if 11 <= int(str(tuple(str(int(m)))[-2]) + str(tuple(str(int(m)))[-1])) <= 19:
            m_new = str(int(m)) + ' минут'

    return  d_new + h_new + m_new

print(counter())