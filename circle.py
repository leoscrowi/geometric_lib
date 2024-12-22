import math
import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_radius(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(2)
        self.assertEqual(res, 4*math.pi)

    def test_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 4*math.pi)


def area(r):
    '''Принимает число r (радиус), возвращает площадь окружности с радиусом r'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r (радиус), возвращает длину окружности с радиусом r'''
    return 2 * math.pi * r

