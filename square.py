import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_radius(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 8)


def area(a):
    '''Принимает сторону квадрата a, возвращает площадь квадрата со стороной a'''
    return a * a


def perimeter(a):
    '''Принимает сторону квадрата a, возвращает периметр квадрата со стороной a'''
    return 4 * a
