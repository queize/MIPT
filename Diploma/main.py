<<<<<<< HEAD
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



=======
import sys

line_arr = []
for line in sys.stdin:
    line_arr.append([x.strip() for x in line.split('/')])

new_line_arr = filter(lambda x: x[1] == line_arr[-1][0], line_arr[:-1])
for line in sorted(new_line_arr, key=lambda x: -x[0]):
    print(line[0])
>>>>>>> 68d3927987612bca30ea39c6e5ba759eeeb9fccc
