# class Person:
#     name = "sofie"
#     print(type("sofie"))
# bajura = Person()
# print(bajura.name)

import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"({self.x},{self.y})"

#
# ohad = Point2D(2, 4)
# meroz = Point2D(3, 6)
# print(ohad, meroz)

    def distance_from(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        return dist

    def __eq__(self, other):
        # print("inside __eq__ of Point2D")
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y

    # def __ne__(self, other):
    #     print("inside __ne__ of Point2D")
    #     return self.x != other.x or self.y != other.y

    def __add__(self, other):
        if not isinstance(other, Point2D):
            return None
        new_point = Point2D(self.x + other.x, self.y + other.y)
        return new_point
    #
    def __len__(self):
         return 2

p1 = Point2D('hello','shalom')
p2 = Point2D(5)
p3 = Point2D(2,2)
p4 = (3,3)
#print(p1, p2)

#p1.translate(3, 3)
#p2.translate(-2, -2)
#print(p1)
#print(p2)

#print(p1.distance_from(p2))
#print(p1.distance_from(p3))
#print(f"p1: {p1}, p2: {p2}, p3: {p3}")
#print(id(p2)==id(p3))
#print(p2+p3)
#print(id(p2))
#print(id(p3))
#print(type(p4))
#print(p1 + "hello")
print(p3+p4)

