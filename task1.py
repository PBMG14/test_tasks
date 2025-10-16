import math
from abc import ABC, abstractmethod
import unittest

"""README При добавлении новой фигуры, функцию рассчета площади писать как calculate_area"""

class Shape(ABC):

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус не должен быть меньше нуля")
        self.radius = radius
    
    def calculate_area(self) -> float:
        return math.pi * self.radius**2
    
    def is_valid(self) -> bool:
        return self.radius > 0 
    
    def __str__(self):
        return f"Круг радиуса {self.radius}"
    
class Triangle(Shape):
    def __init__(self, a:float, b:float, c:float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Все стороны должны быть больше нуля")
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def calculate_area(self) -> float:
        p = (self.side_a + self.side_b + self.side_c)/2
        return math.sqrt(p*(p-self.side_a)*(p-self.side_b)*(p-self.side_c))
    
    def is_valid(self) -> bool:
        return (self.side_a > 0 and self.side_b > 0 and self.side_c > 0 and self.side_a + self.side_b > self.side_c
            and self.side_b + self.side_c > self.side_a
            and self.side_a + self.side_c > self.side_b)
    
    def is_Right(self):
        sides = sorted[self.side_a, self.side_b, self.side_c]
        return (sides[1]**2+sides[0]**2 == sides[2]**2)
    
    def __str__(self):
        return f"Треугольник со сторонами:{self.side_a}, {self.side_b}, {self.side_c}"
    
class Factory:

    @staticmethod
    def create_circle(radius: float) -> Circle:
        return Circle(radius)
    
    @staticmethod
    def create_triangle(side_a: float, side_b: float, side_c: float) -> Triangle:
        return Triangle(side_a, side_b, side_c)
    
    @staticmethod
    def create_shape(shape_type: str, *args) -> Shape:
        creator = {
            'circle': lambda: Circle(args[0]),
            'triangle': lambda: Triangle(args[0], args[1], args[2])
        }
        if shape_type not in creator:
            raise ValueError(f"Не знаю такую фигуру")
        return creator[shape_type]()

class Calculator:

    def calculate(shape : Shape):
        if not Shape.is_valid():
            raise ValueError("Фигуры не существует")
        return Shape.calculate_area()

class TestGeometryLibrary(unittest.TestCase):
    def test_creation_1(self):
        circle = Circle(5.0)
        self.assertEqual(circle.radius, 5.0)
    
    def test_triangle_creation(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.side_a, 3)
        self.assertEqual(triangle.side_b, 4)
        self.assertEqual(triangle.side_c, 5)


if __name__ == '__main__':
    unittest.main()
