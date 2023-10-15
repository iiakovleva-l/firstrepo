# Файл: test_math.py

def add(x, y):
    """Функция сложения двух чисел."""
    return x + y

def test_add_positive_numbers():
    assert add(1, 2) == 3

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_mixed_numbers():
    assert add(1, -1) == 0
    assert add(0, 0) == 0
