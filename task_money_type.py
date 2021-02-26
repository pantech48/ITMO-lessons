class OperandTypeError(TypeError):

class MoneyArithmeticError(ArithmeticError):

class Money:

    def __init__(self, whole, fracton=0):
        self._whole = whole
        self._fraction = fracton

    def __add__(self, other):
        if type(self) != type(other):
            raise OperandTypeError('')
        return Money(self._whole + other._whole, self._fraction + other._fracton)

    def __sub__(self,other):
        if type(self) != type(other):
            raise OperandTypeError('')
        return Money(self._whole - other._whole, self._fraction - other._fracton)

    def __mul__(self, number):
        if not (type(number) == type(int) or type(number) == type(float)):
            raise OperandTypeError('')
        mult = self._whole + self._fraction * 10**(-)
        return Money(self._whole - other._whole, self._fraction - other._fracton)

    def __truediv__(self, other):

    def __eq__(self, other):

    def __gt__(self, other):

    def __ge__(self, other):

    def __repr__(self):

    def get_whole(self):

    def get_fraction(self):
