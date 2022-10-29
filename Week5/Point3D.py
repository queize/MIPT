# Реализуйте класс Point3D, представляющий точку в трехмерном пространстве. 
# Конструктор должен принимать три аргумента: x, y и z — координаты точки. 
# Класс должен реализовывать метод distance_to, принимающий в качестве аргумента другую точку и возвращающий расстояние между ними.

# Подробнее про вычисление расстояния можно прочитать в источнике.

import math

class Point3D:
    def __init__(self, x, y, z) -> None:
        self.x, self.y, self.z = x, y, z
    

    def distance_to(self, other) -> float:
        return math.sqrt(
            (self.x - other.x)**2 + 
            (self.y - other.y)**2 + 
            (self.z - other.z)**2)



class Segment3D:
    def __init__(self, p1: Point3D, p2: Point3D):
        self.p1 = p1
        self.p2 = p2
    

    def length(self):
        return self.p1.distance_to(self.p2)


    def middle(self):
        x1, x2 = self.p1.x, self.p2.x
        y1, y2 = self.p1.y, self.p2.y
        z1, z2 = self.p1.z, self.p2.z
        return Point3D((x1 + x2)/2, (y1 + y2)/2, (z1 + z2)/2)


    def cos_to(self, other):
        dist1 = self.length()
        dist2 = other.length()
        scal =      (self.p2.x - self.p1.x) * (other.p2.x - other.p1.x) \
                +   (self.p2.y - self.p1.y) * (other.p2.y - other.p1.y) \
                +   (self.p2.z - self.p1.z) * (other.p2.z - other.p1.z)
        return abs(scal / (dist1 * dist2) )




