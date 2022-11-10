import math

class Vector:

    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(other * self.x, other * self.y)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return self + (-other)
        else:
            return NotImplemented
    
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __truediv__(self, num):
        if isinstance(num, int):
            return Vector(self.x / num, self.y / num)
        else:
            return NotImplemented
