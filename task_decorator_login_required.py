import hashlib

def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()

with_err = 1

def login_required(func):
    def wrapper(*args, **kwargs):
        with open('token.txt') as f:
            auth = f.read().strip('\n ')
        global with_err
        misstake = 0
        while with_err:
            login = input()
            password = input()
            if make_token(login, password) == auth:
                with_err = 0              
            else:
                misstake += 1
                if misstake == 3:
                    raise RuntimeError('Authentication failed')   
        return func(*args, **kwargs)       
    return wrapper


