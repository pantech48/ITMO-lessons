class Matrix:

    def __init__(self, value):
        self._value = value

    def __add__(self, other):

        def matrix_size(matrix):
            line = len(matrix._value)
            column = len(matrix._value[0])
            return line, column

        if matrix_size(self) == matrix_size(other):

            add = list(zip(self, other))
            for j, k in enumerate(add):
                add[j] = add[j][j][j] + add[j][j+1][j]
            
            for j, k in enumerate(self):
                for j, k in enumerate(other):


    def __sub__(self, other):

    def __mul__(self, other):

    def get_transpose_matrix(self):
        for m, n

    def tolist(self):



class MatrixSizeError(ArithmeticError):





class OperandTypeError(TypeError):

