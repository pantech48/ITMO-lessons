from math import pi


class Figure:
    def __init__(self):
        """Инициализатор."""

    def get_area(self):
        raise NotImplementedError

    def get_perimeter(self):
        raise NotImplementedError

class Rectangle(Figure):

    def __init__(self, a, b):
        self._a = a
        self._b = b
    
    def get_area(self):
        return self._a * self._b

    def get_perimeter(self):
        return (self._a + self._b) * 2


class Triangle(Figure):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def get_area(self):
        p = self.get_perimeter()/2
        return (p*(p - self._a)*(p - self._b)*(p - self._c)) ** .5

    def get_perimeter(self):
        return self._a + self._b + self._c
        

class Circle(Figure):

    def __init__(self, r):
        self._r = r

    def get_area(self):
        return pi * (self._r ** 2)

    def get_perimeter(self):
        return 2 * pi * self._r