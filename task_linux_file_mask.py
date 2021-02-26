class MaskItem:

    def __init__(self, mask=0):
        self._mask = mask

    def is_readable(self):
        return True if self._mask > 3 else False
        
    def is_writable(self):
        return True if self._mask == 2 or self._mask == 3 or self._mask == 6 or self._mask == 7 else False
        
    def is_executable(self):
        return True if self._mask == 1 or self._mask == 3 or self._mask == 7 or self._mask == 5 else False

    def __str__(self):
        if self._mask > 3:
            r = 'r'  
        else:
            r = '-'
        if self._mask == 2 or self._mask == 3 or self._mask == 6 or self._mask == 7:
            w = 'w'  
        else:
            w = '-'
        if self._mask == 1 or self._mask == 3 or self._mask == 7 or self._mask == 5:
            x = 'x'  
        else:
            x = '-'
        return f'{r}{w}{x}'
    
    def __repr__(self):
        if self._mask == 0:
            return f'{self.__class__.__name__}()'
        return f'{self.__class__.__name__}({bin(self._mask)})'

class Mask:

    def __init__(self, author, group, other):
        self._author = author
        self._group = group
        self._other = other

    def __str__(self):
        return f'{self._author.__str__()}{self._group.__str__()}{self._other.__str__()}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self._author.__repr__()}, {self._group.__repr__()}, {self._other.__repr__()})'

