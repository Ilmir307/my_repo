"""Пример программы на Python по стандартам PEP 8 (задание 1668)."""


def square(number):
    """Возвращает квадрат числа."""
    return number * number


def cube(number):
    """Возвращает куб числа."""
    return number ** 3


def main():
    """Точка входа: демонстрирует работу функций."""
    print("Квадрат 7:", square(7))
    print("Куб 3:", cube(3))


if __name__ == "__main__":
    main()
