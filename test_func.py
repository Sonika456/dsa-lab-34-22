"""Тесты для функции get_triangle_type с использованием unittest."""
import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestGetTriangleType(unittest.TestCase):
    """Набор тестов для проверки функции определения типа треугольника."""

    # Позитивные тесты
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")

    def test_isosceles(self):
        self.assertEqual(get_triangle_type(4, 4, 6), "isosceles")

    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    # Негативные тесты
    def test_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 4, 5)

    def test_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 4, 5)

    def test_inequality_violation(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

    def test_non_numeric(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("text", 4, 5)


if __name__ == "__main__":
    unittest.main()