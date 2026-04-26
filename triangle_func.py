"""Модуль с функцией определения типа треугольника."""

class IncorrectTriangleSides(Exception):
    """Выбрасывается при передаче некорректных длин сторон."""
    pass


def _validate_sides(a: float, b: float, c: float) -> None:
    """Внутренняя проверка корректности сторон."""
    if not all(isinstance(side, (int, float)) for side in (a, b, c)):
        raise IncorrectTriangleSides("Стороны должны быть числовыми значениями.")
    if any(side <= 0 for side in (a, b, c)):
        raise IncorrectTriangleSides("Длины сторон должны быть строго положительными.")
    if not (a + b > c and a + c > b and b + c > a):
        raise IncorrectTriangleSides("Нарушено неравенство треугольника.")


def get_triangle_type(a: float, b: float, c: float) -> str:
    """
    Определяет тип треугольника по трём сторонам.
    Возвращает: 'equilateral', 'isosceles' или 'nonequilateral'.
    """
    _validate_sides(a, b, c)
    
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"