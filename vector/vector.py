import numpy as np

class Vector(object):
    def __init__(self, array):
        self.array = np.array(array, dtype=float)

    def __str__(self):
        return f"({'; '.join(map(str, self.array))})"

    def __repr__(self):
        return f"({'; '.join(map(str, self.array))})"

    def __pos__(self):
        return self.array

    def __neg__(self):
        return -self.array

    def __abs__(self):
        return abs(self.array)

    def __invert__(self):
        return ~self.array

    def __lt__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.module() < other
        elif isinstance(other, str):
            try:
                other = float(other)
                return self.module() < other
            except:
                return "Value Error, you can't compare Vector to letters or symbols"
        elif isinstance(other, Vector) or isinstance(other, list) or isinstance(other, tuple) or isinstance(other, np.ndarray):
            return self.module() < other.module() if isinstance(other, Vector) else self.module() < sum(other)

    def __le__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.module() <= other
        elif isinstance(other, str):
            try:
                other = float(other)
                return self.module() <= other
            except:
                return "Value Error, you can't compare Vector to letters or symbols"
        elif isinstance(other, Vector) or isinstance(other, list) or isinstance(other, tuple) or isinstance(other, np.ndarray):
            return self.module() <= other.module() if isinstance(other, Vector) else self.module() <= sum(other)

    def __eq__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.module() == other
        elif isinstance(other, str):
            try:
                other = float(other)
                return self.module() == other
            except:
                return "Value Error, you can't compare Vector to letters or symbols"
        elif isinstance(other, Vector) or isinstance(other, list) or isinstance(other, tuple) or isinstance(other, np.ndarray):
            return self.module() == other.module() if isinstance(other, Vector) else self.module == sum(other)

    def __ne__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.module() != other
        elif isinstance(other, str):
            try:
                other = float(other)
                return self.module() != other
            except:
                return "Value Error, you can't compare Vector to letters or symbols"
        elif isinstance(other, Vector) or isinstance(other, list) or isinstance(other, tuple) or isinstance(other, np.ndarray):
            return self.module() != other.module() if isinstance(other, Vector) else self.module() != sum(other)

    def __gt__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.module() > other
        elif isinstance(other, str):
            try:
                other = float(other)
                return self.module() > other
            except:
                return "Value Error, you can't compare Vector to letters or symbols"
        elif isinstance(other, Vector) or isinstance(other, list) or isinstance(other, tuple) or isinstance(other, np.ndarray):
            return self.module() > other.module() if isinstance(other, Vector) else self.module() > sum(other)

    def __ge__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.module() >= other
        elif isinstance(other, str):
            try:
                other = float(other)
                return self.module() >= other
            except:
                return "Value Error, you can't compare Vector to letters or symbols"
        elif isinstance(other, Vector) or isinstance(other, list) or isinstance(other, tuple) or isinstance(other, np.ndarray):
            return self.module() >= other.module() if isinstance(other, Vector) else self.module() >= sum(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __len__(self):
        return len(self.array)

    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.array - other
        elif isinstance(other, str):
            try:
                other = float(other)
                return self.array - other
            except:
                return "Value Error, it can't sub Vector with letters or symbols"

        elif isinstance(other, Vector) or isinstance(other, list) or isinstance(other, tuple) or isinstance(other, np.ndarray):
            if len(self) == len(other):
                return self.array - other.array if isinstance(other, Vector) else self.array - other
            else:
                return 'They should have same sizes'

    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.array + other
        elif isinstance(other, str):
            try:
                other = float(other)
                return self.array + other
            except:
                return "Value Error, it can't sum Vector with letters or symbols"

        elif isinstance(other, Vector) or isinstance(other, list) or isinstance(other, tuple) or isinstance(other, np.ndarray):
            if len(self) == len(other):
                return self.array + other.array if isinstance(other, Vector) else self.array + other
            else:
                return 'They should have same sizes'

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.array * other
        elif isinstance(other, str):
            try:
                other = float(other)
                return self.array * other
            except:
                return "Value Error, it can't sum Vector with letters or symbols"

        elif isinstance(other, Vector) or isinstance(other, list) or isinstance(other, tuple) or isinstance(other, np.ndarray):
            if len(self) == len(other):
                return self.array * other.array if isinstance(other, Vector) else self.array * other
            else:
                return 'They should have same sizes'

    def module(self):
        return np.linalg.norm(self.array)

    def dot_product(self, other):
        if isinstance(other, Vector):
            return np.dot(self.array, other.array)
        else:
            return 'It should be Vector, to find!'

    def vector_product(self, other):
        if isinstance(other, Vector):
            return np.vdot(self.array, other.array)
        else:
            return 'It should be Vector, to find!'

    def distance(self, other):
        if isinstance(other, Vector):
            return np.linalg.norm(self.array - other.array)
        else:
            return 'It should be Vector, to find!'


a = Vector([1, 1, 1])
b = Vector([2, 0, 0])
print(a)
print(~a)
print(len(a))
print(a+b)
print(a-b)
print(a*b)
print(a*3)
print(a>b)
print(a.module())
print(a.dot_product(b))
print(a.vector_product(b))
print(a.distance(b))
