import math

# Спросим, что хорошего в этой библиотеке
print(math.__doc__)

# Будет напечатано:
# This module provides access to the mathematical functions
# defined by the C standard. 
math.sqrt.__doc__
"""Документация модуля. Описывает работу классов и функций. 
Размещается в верхней части файла (начиная с первой строки).
"""
def tricky_func(self):
    """Описывает работу функции tricky_func."""
    ...


class Test:
    """Класс Test используется для демонстрации docstring."""

    def first(self):
        """Описывает метод first и демонстрирует перенос строки 
        документации.
        """
        ...


print(__doc__)
print(tricky_func.__doc__)
print(Test.__doc__)
print(Test.first.__doc__)