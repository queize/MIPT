# Реализуйте класс Point3D, представляющий точку в трехмерном пространстве. Конструктор должен принимать три аргумента: 
# x, y и z — координаты точки. Класс должен реализовывать метод distance_to, 
# принимающий в качестве аргумента другую точку и возвращающий расстояние между ними.


import math

class Point3D:
    def __init__(self, x, y, z) -> None:
        self._x = x
        self._y = y
        self._z = z
    

    def distance_to(self, other) -> float:
        return math.sqrt((self._x - other._x)**2  /
            + (self._y - other._y)**2 /
            + (self._z - other._z)**2)



