"""Модуль с классом Triangle."""
from triangle_func import IncorrectTriangleSides, _validate_sides


class Triangle:
    """Класс, описывающий треугольник."""

    def __init__(self, a: float, b: float, c: float):
        """Конструктор. Вызывает исключение при некорректных данных."""
        _validate_sides(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self) -> str:
        """Возвращает тип треугольника."""
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        return "nonequilateral"

    def perimeter(self) -> float:
        """Возвращает периметр треугольника."""
        return self.a + self.b + self.c