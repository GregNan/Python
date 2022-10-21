# class MyClass:
#     def __init__(self, param):
#         self.param = param
# obj = MyClass(.1)
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
# который должен принимать данные (список списков) для формирования матрицы.
# [[], [], []]
# Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add()__ для реализации операции
# сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

# from typing import List


# class Matrix:
#     def __init__(self, matrix_data: List[List]):
#         self.__matrix = matrix_data

#         m_rows = len(self.__matrix)
#         self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

#         if len(self.__matrix_size) != 1:
#             raise ValueError("Invalid matrix size")

#     def __add__(self, other: "Matrix") -> "Matrix":
#         if not isinstance(other, Matrix):
#             raise TypeError(f"'{other.__class__.__name__}' "
#                             f"incompatible object type")
#         if self.__matrix_size != other.__matrix_size:
#             raise ValueError(f"Matrix sizes difference")

#         result = []

#         for item in zip(self.__matrix, other.__matrix):
#             result.append([sum([j, k]) for j, k in zip(*item)])

#         return Matrix(result)

#     def __str__(self) -> str:
#         return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


# if __name__ == '__main__':
#     matrix1 = Matrix([[1, 2], [3, 4]])
#     print(matrix1, '\n')

#     matrix2 = Matrix([[10, 20], [30, 40]])
#     print(matrix2, '\n')

#     print(matrix1 + matrix2)

# Задание 2.
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Единственный класс этого проекта — одежда (класс Clothes).
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
# для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать
# абстрактный класс для единственного класса проекта,
# проверить на практике работу декоратора @property
# Пример:
# Расход ткани на пальто = 1.27
# Расход ткани на костюм = 20.30
# Общий расход ткани = 21.57
# Два класса: абстрактный и Clothes

# from abc import ABC, abstractmethod

# from typing import Any


# class AbstractClothes(ABC):
#     """ Интерфейс одежды """
#     @property
#     @abstractmethod
#     def tissue_required(self):
#         pass

#     @property
#     @abstractmethod
#     def measuring(self):
#         """ Общая размерность одежды """
#         pass

#     @abstractmethod
#     def _calc_tissue_required(self):
#         pass


# class Clothes(AbstractClothes):
#     _clothes = []

#     """ Одежда """
#     def __init__(self, name: str, measuring: Any):
#         self.name = name
#         self._measuring = measuring
#         self._tissue_required = None

#         self._clothes.append(self)

#     def _calc_tissue_required(self):
#         raise NotImplemented

#     @property
#     def tissue_required(self) -> float:
#         """ Расход ткани """
#         if not self._tissue_required:
#             self._calc_tissue_required()

#         return self._tissue_required

#     @property
#     def measuring(self) -> Any:
#         """ Узнать размер """
#         return self._measuring

#     @measuring.setter
#     def measuring(self, measuring: Any):
#         """ Установить новый размер пальто """
#         self._measuring = measuring
#         self._tissue_required = None

#     @property
#     def total_tissue_required(self):
#         """ Ткани на всю одежду """
#         return sum([item.tissue_required for item in self._clothes])


# class Coat(Clothes):
#     """ Пальто """
#     def _calc_tissue_required(self):
#         """ посчитать расход ткани для пальто """
#         self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

#     @property
#     def V(self) -> Any:
#         """ Узнать размер пальто """
#         return self.measuring

#     @V.setter
#     def V(self, size: Any):
#         """ Установить новый размер пальто """
#         self.measuring = size

#     def __str__(self):
#         return f"Для пошива пальто {self.measuring} размера " \
#                f"требуется {self.tissue_required} кв. метров ткани"


# class Suit(Clothes):
#     """ Костюм """
#     def _calc_tissue_required(self):
#         """ посчитать расход ткани для костюма """
#         self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

#     @property
#     def H(self) -> Any:
#         """ Узнать размер костюма """
#         return self.measuring

#     @H.setter
#     def H(self, height: Any):
#         """ Установить новый размер костюма """
#         self.measuring = height

#     def __str__(self):
#         return f"Для пошива костюма на рост {self.measuring} см. " \
#                f"требуется {self.tissue_required} кв. метров ткани"


# if __name__ == '__main__':
#     coat = Coat('Пальто от Ш', 8)
#     print(coat)
#     coat.V = 10
#     print(coat)

#     suit = Suit('Костюм от Б', 180)
#     print(suit)
#     suit.H = 180
#     print(suit)

#     print(coat.total_tissue_required)
#     print(suit.total_tissue_required)

# Задание 3.
# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка (Cell).
# В его конструкторе инициализировать параметр (quantity),
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()),
# вычитание (sub()),
# умножение (mul()),
# деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# ** - По желанию: В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

# class Cell:
#     def __init__(self, quantity):
#         self.quantity = int(quantity)
#         #self.result = result

#     def __str__(self):
#         return f'Результат операции {self.quantity * "*"}'

#     def __add__(self, other):
#         # self.result = Cell(self.quantity + other.quantity)
#         return Cell(self.quantity + other.quantity)

#     def __sub__(self, other):
#         '''
#         Выдает ошибку о том, что результат не число  при вычислении
#         if int(Cell(self.quantity - other.quantity)) > 0:
#             return Cell(int(self.quantity - other.quantity))
#         else:
#             return f'Операция вычитания невозможна'""
#         '''
#         return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

#         # return Cell(int(self.quantity - other.quantity))

#     def __mul__(self, other):
#         #self.result = Cell(int(self.quantity * other.quantity))
#         return Cell(int(self.quantity * other.quantity))

#     def __truediv__(self, other):
#         #self.result = Cell(round(self.quantity // other.quantity))
#         return Cell(round(self.quantity // other.quantity))


#     def make_order(self, cells_in_row):
#         row = ''
#         for i in range(int(self.quantity / cells_in_row)):
#             row += f'{"*" * cells_in_row} \\n'
#         row += f'{"*" * (self.quantity % cells_in_row)}'
#         return row

# cells1 = Cell(33)
# cells2 = Cell(9)
# print(cells1)
# print(cells1 + cells2)
# print(cells2 - cells1)
# print(cells2.make_order(5))
# print(cells1.make_order(10))
# print(cells1 / cells2)