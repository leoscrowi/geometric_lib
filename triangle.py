import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_radius(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(2, 1)
        self.assertEqual(res, 1)

    def test_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

def area(a, h):
    '''Принимает сторону a, к которой проведена высота h и возвращает площадь треугольника'''
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает три стороны треугольника a, b, c и возвращает периметр треугольника со сторонами a, b, c'''
    return a + b + c
