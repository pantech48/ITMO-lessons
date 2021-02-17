import hashlib


def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()
  


fail = 1

def login_required(func):
    def wrapper(*args, **kwargs):
        global fail
        fail_count = 0    
        while fail:
            with open('token.txt') as f:
                auth = f.read().strip('\n ')
            username, password = input(), input()
            user_data = make_token(username, password)
            if user_data == auth:
                fail = 0
                break
            else:
                fail_count += 1
            if fail_count >= 3:
                raise RuntimeError('Authentication failed')
        return func(*args, **kwargs)
    return wrapper