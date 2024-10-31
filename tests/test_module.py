import unittest
from src.module import calculate_area


class TestCalculateArea(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(calculate_area("circle", 3), 28.274333882308138)

    def test_square_area(self):
        self.assertEqual(calculate_area("square", 4), 16)

    def test_rectangle_area(self):
        self.assertEqual(calculate_area("rectangle", 3, 5), 15)

    def test_invalid_shape(self):
        with self.assertRaises(ValueError):
            calculate_area("triangle", 3, 4, 5)

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            calculate_area("circle", 3, 4)


if __name__ == '__main__':
    unittest.main()
