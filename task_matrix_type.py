class MatrixSizeError(ArithmeticError):
    """Matrix size error class."""
    def __init__(self):
        super().__init__('Incompatible matrix size')


class OperandTypeError(TypeError):
    """Operand type error class."""
    def __init__(self, operand, operator):
        super().__init__(
            f"unsupported operator type(s) for {operator}: '{Matrix.__name__}' and '{type(operand).__name__}'"
        )


class Matrix:
    """Class Matrix"""

    def __init__(self, value):
        """Inizializator of 'Matrix' object"""
        self._value = value

    def size(self):
        """Size of matrix."""
        size = {
            'columns': len(self._value[0]),
            'rows': len(self._value)
        }
        return size

    def __add__(self, other):
        """Addition operator."""

        if not isinstance(other, Matrix):
            raise OperandTypeError(other, '+')

        if self.size() != other.size:
            raise MatrixSizeError

        result = [[self._value[i][j] + other._value[i][j] for j in range(self.size()['columns'])] for i in range(other.size()['rows'])]
        return Matrix(result)


    def __sub__(self, other):
        """Substraction operator."""

        if not isinstance(other, Matrix):
            raise OperandTypeError(other, '-')

        if self.size() != other.size:
            raise MatrixSizeError

        result = [[self._value[i][j] - other._value[i][j] for j in range(self.size()['columns'])] for i in range(other.size()['rows'])]
        return Matrix(result)

    def __mul__(self, other):
        """Multiplication operator."""

        if not (isinstance(other, Matrix) or isinstance(other, int) or isinstance(other, float)):
            raise OperandTypeError(other, '*')

        if isinstance(other, Matrix):

            if len(self.get_transpose_matrix()._value) != len(other._value):
                raise MatrixSizeError()

            result = [[sum(a*b for a,b in zip(self_raw,other_col)) for other_col in zip(*other._value)] for self_raw in self._value]
            return Matrix(result)
        
        result = [[elem*other for elem in row] for row in self._value]
        return Matrix(result)

    def get_transpose_matrix(self):
        """Transpose operator."""
        trans_matr = list(map(list, zip(*self._value)))
        return Matrix(trans_matr)
        
    def tolist(self):
        """Return matrix as 2D list."""
        return self._value

a = Matrix([
    [1, -1],
    [2, 0],
    
])

b = Matrix([
    [1, -1],
    [2, 0],
    
])

c = a * 3
print(c.tolist() is c)

