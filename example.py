"""Пример программы на Python, оформленной по стандартам PEP 8.

Задание 1641: работа с Git и применение стандартов кодирования.
"""


def sum_numbers(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


def subtract_numbers(a, b):
    """Возвращает разность двух чисел."""
    return a - b


def main():
    """Точка входа: демонстрирует работу функций."""
    result = sum_numbers(3, 5)
    print("Сумма 3 и 5 равна", result)
    print("Разность 10 и 4 равна", subtract_numbers(10, 4))


if __name__ == "__main__":
    main()
