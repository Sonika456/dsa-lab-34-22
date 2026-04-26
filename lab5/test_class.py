"""Тесты для класса Triangle с использованием pytest."""
import pytest
from triangle_class import Triangle
from triangle_func import IncorrectTriangleSides


class TestTriangleClass:
    """Набор позитивных и негативных тестов для класса Triangle."""

    # Позитивные тесты
    def test_equilateral(self):
        t = Triangle(5, 5, 5)
        assert t.triangle_type() == "equilateral"
        assert t.perimeter() == 15

    def test_isosceles(self):
        t = Triangle(4, 4, 6)
        assert t.triangle_type() == "isosceles"
        assert t.perimeter() == 14

    def test_nonequilateral(self):
        t = Triangle(3, 4, 5)
        assert t.triangle_type() == "nonequilateral"
        assert t.perimeter() == 12

    def test_float_sides(self):
        t = Triangle(2.5, 2.5, 4.0)
        assert t.triangle_type() == "isosceles"
        assert t.perimeter() == pytest.approx(9.0)

    # Негативные тесты (проверка исключений в конструкторе)
    def test_negative_side(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(-2, 4, 5)

    def test_zero_side(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(0, 5, 5)

    def test_inequality_violation(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(10, 2, 3)

    def test_non_numeric(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle("a", 4, 5)



            