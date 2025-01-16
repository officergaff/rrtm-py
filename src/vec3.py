import math

class Vec3:
    def __init__(self, e0=0.0, e1=0.0, e2=0.0):
        self.e = [e0, e1, e2]

    def x(self):
        return self.e[0]
    def y(self):
        return self.e[1]
    def z(self):
        return self.e[2]

    def length(self):
        return math.sqrt(self.length_squared())
    def length_squared(self):
        return self.x()**2 + self.y()**2 + self.z()**2

    @staticmethod
    def unit_vector(u):
        return u / u.length()
    @staticmethod
    def dot(u, v):
        return (u[0] * v[0]) + (u[1] * v[1]) + (u[2] * v[2])
    @staticmethod
    def cross(u, v):
        return Vec3(u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])

    # Vector addition and substraction
    def __add__(self, other):
        return Vec3(self[0] + other[0], self[1] + other[1], self[2] + other[2])
    def __sub__(self, other):
        return Vec3(self[0] - other[0], self[1] - other[1], self[2] - other[2])

    # Overloading __mul__ for both scalar and Vec3 operations
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vec3(self[0] * other, self[1] * other, self[2] * other)
        if isinstance(other, Vec3):
            return Vec3(self[0] * other[0], self[1] * other[1], self[2] * other[2])
        else:
            raise TypeError(f"Unsupported operands type(s) for *: 'Vec3' and {type(other).__name__}")
    # Only scalar division
    def __truediv__(self, t: float):
        return Vec3(self.x() / t, self.y() / t, self.z() / t)

    def __neg__(self):
        return Vec3(-self.x(), -self.y(), -self.z())
    def __getitem__(self, i):
        return self.e[i]
    def __setitem__(self, i, value):
        self.e[i] = value

    # In-place operators
    def __iadd__(self, other):
        self.e[0] += other.e[0]
        self.e[1] += other.e[1]
        self.e[2] += other.e[2]
        return self
    def __isub__(self, other):
        self.e[0] -= other.e[0]
        self.e[1] -= other.e[1]
        self.e[2] -= other.e[2]
        return self
    def __imul__(self, t):
        self.e[0] += t
        self.e[1] += t
        self.e[2] += t
        return self
    def __itruediv__(self, t):
        return self.__imul__(1.0/t)
    
    def __repr__(self):
        return f"Vec3({self.x()}, {self.y()}, {self.z()})"
    def __str__(self):
        return f"{self.x()} {self.y()} {self.z()}"

Point = Vec3
