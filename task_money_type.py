class OperandTypeError(TypeError):
    """Operand type error class."""
    def __init__(self, operand, operator=None):
        if operator is not None:
            super().__init__(
                f"unsupported operator type(s) for {operator}: '{Money.__name__}' and '{type(operand).__name__}'"
            )
        else:
            super().__init__(
                f"comparison not supported between instances of '{Money.__name__}' and '{type(operand).__name__}'"
            )
        

class MoneyArithmeticError(ArithmeticError):
    """Money arithmetic error class."""
    def __init__(self):
        super().__init__('The coefficient should be positive')


class Money:
    """Money class."""

    def __init__(self, whole, fraction=0):
        """Initialize object 'Money'."""
        self._whole = whole 
        self._fraction = fraction
        self._int_curency = self._whole * 100 + self._fraction

    def get_whole(self):
        """Getter for whole attr."""
        return self._int_curency // 100

    def get_fraction(self):
        """Getter for frection attr."""
        return self._int_curency - self.get_whole()*100

    def __repr__(self):
        """Representation of object 'Money'."""
        return '{}({}, {})'.format(
                                self.__class__.__name__,
                                self.get_whole(),     
                                self.get_fraction()
                                )

    def __add__(self, other):
        """Addition operator."""

        if not isinstance(other, Money):
            raise OperandTypeError(other, '+')

        add = self._int_curency + other._int_curency
        result = Money(0, add)
        return Money(result.get_whole(), result.get_fraction())

    def __sub__(self,other):
        """Division operator."""

        if not isinstance(other, Money):
            raise OperandTypeError(other, '-')

        sub = self._int_curency + other._int_curency
        result = Money(0, sub)
        return Money(result.get_whole(), result.get_fraction())

    def __mul__(self, number):
        """Division operator."""
        
        if not (isinstance(number, int) or isinstance(number, float)):
            raise OperandTypeError(number, '*')

        mult = self._int_curency * number
        result = Money(0, mult)
        return Money(result.get_whole(), result.get_fraction())
        

    def __truediv__(self, other):
        """Division operator."""

        if not (isinstance(other, int) or isinstance(other, Money)):
            raise OperandTypeError(other, '/')

        if isinstance(other, Money):
            result = self._int_curency / other._int_curency
            return float(result)
        
        if other <= 0:
            raise MoneyArithmeticError()

        div = round(self._int_curency / other)
        result = Money(0, div)
        return Money(result.get_whole(), result.get_fraction())


    def __eq__(self, other):
        """Division operator."""

        if not isinstance(other, Money):
            raise OperandTypeError(other)

        result = self._int_curency == other._int_curency
        return result



    def __gt__(self, other):
        """Division operator."""

        if not isinstance(other, Money):
            raise OperandTypeError(other)

        result = self._int_curency > other._int_curency
        return result

    def __ge__(self, other):
        """Division operator."""

        if not isinstance(other, Money):
            raise OperandTypeError(other)

        result = self._int_curency >= other._int_curency
        return result




money1 = Money(593, 72)

money2 = Money(0, 455)

a = money1 / 74

print(money1 != money2)
print(a)
