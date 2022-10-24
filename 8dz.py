# расчёт зарплаты
# from collections import namedtuple
import unittest

# Salary = namedtuple('Salary', ('surname', 'name', 'worked', 'rate'))

# def get_salary(line):
#     line = line.split()
#     if line:
#         data = Salary(*line)
#         fio = ''.join((data.surname, data.name))
#         salary = int(data.worked) * int(data.rate)
#         res = (fio, salary)
#     else:
#         res = ()
#     return res

# class TestSalary(unittest.TestCase):
#     def test_get_salary_summ(self):
#         self.assertEqual(get_salary('Лютиков Руслан 60 1000'),('Лютиков Руслан', 60000))
#     def test_get_salary_fio(self):
#         self.assertEqual(get_salary('Лютиков Руслан 60 1000')[0],'Лютиков Руслан')
#     def test_get_salary_empty(self):
#         self.assertEqual(get_salary(''), ())

# if __name__ == '__main__':
#     unittest.main()

# Вывести квадрат числа
# number = 2
# print('Квадрат числа {} равен {}'.format(number, number**2))
# print(f'Квадрат числа {number} равен {number**2}')
# print('Квадрат числа', number, 'равен', number**2)

# class TestKvadrat(unittest.TestCase):
#     def test_get_kvadrat(self):
#         self.assertEqual(number**2, 4)

# if __name__ == '__main__':
#     unittest.main()


# 2 принимает 5 чисел и находит максимальное из них
# list = [1,4,8,7,50]
# max = list[0]
# for i in list:
#    if max < i:
#        max = i
# print (f"Максимальное число равно {max}")
# class TestMax(unittest.TestCase):
#     def test_get_max(self):
#         self.assertEqual(50, 50)

# if __name__ == '__main__':
#     unittest.main()


#3 на вход дробь и показывает первую цифру дробной части
# a = float(input("Введите дробное число с точкой"))
# n = int(a * 10 %10)
# print(n)
# class Testdrob(unittest.TestCase):
#     def test_get_drob(self):
#         self.assertEqual(1, 1)

# if __name__ == '__main__':
#     unittest.main()

# # 4 кратно ли число 5,10,15 но не 30
# c = int(input("a ="))
# if ((c%5==0 and c%10==0) or c%15==0) and c%30!=0:
#    print('кратно число 5,10,15 но не 30')
# class TestMax(unittest.TestCase):
#     def test_get_krat(self):
#         self.assertEqual(c, 75)

# if __name__ == '__main__':
#     unittest.main()
# 5  (1+2)*3
# def parse(s):
#     result = []
#     digit = ''
#     for symb in s:
#         if symb.isdigit():
#             digit += symb
#         elif symb in ['(',')']:
#             if digit:
#                 result.append(float(digit))
#                 digit = ''
#             result.append(symb)
#         else:
#             if digit:
#                 result.append(float(digit))
#             digit = ''
#             result.append(symb)
#     else:
#         if digit:
#             result.append(float(digit))
#     return result
# s = "(1+2)*3"
# print(parse(s))
    
# class TestParse(unittest.TestCase):
#     def test_get_parse(self):
#         self.assertEqual(parse(s), ['(', 1.0, '+', 2.0, ')', '*', 3.0])

# if __name__ == '__main__':
#     unittest.main()
# 6 
# def calc(lst):
#     result = 0.0
#     while '*' in lst:
#         index = lst.index('*')
#         result = lst[index -1] * lst[index + 1]
#         lst = lst[:index - 1] + [result] + lst[index + 2:]
#     while '/' in lst:
#         index = lst.index('/')
#         result = lst[index -1] / lst[index + 1]
#         lst = lst[:index - 1] + [result] + lst[index + 2:]
#     while '+' in lst:
#         index = lst.index('+')
#         result = lst[index -1] + lst[index + 1]
#         lst = lst[:index - 1] + [result] + lst[index + 2:]
#     while '-' in lst:
#         index = lst.index('-')
#         result = lst[index -1] - lst[index + 1]
#         lst = lst[:index - 1] + [result] + lst[index + 2:]
#     return result

# def brackets(lst):
#     while '(' in lst:
#         opening = lst.index('(')
#         closing = lst.index(')')
#         lst = lst[:opening] + [calc(lst[opening + 1:closing])] + lst[closing + 1:]
#         return lst

# # s = "(1+2)*3"
# # result = parse(s)
# # result = brackets(result)
# # print(calc(result))
# # print(parse("(1+2)*3"))
# result = ['(', 1.0, '+', 2.0, ')', '*', 3.0]
# class TestCalc(unittest.TestCase):
#     def test_get_calc(self):
#         self.assertEqual(brackets(calc(result)), 9)

# if __name__ == '__main__':
#     unittest.main()
# 7,8,9,10
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume

r = MassCount(7, 4, 6)
print(r.mass())

class Test(unittest.TestCase):
    def test_get_init(self):
        self.assertEqual(self._length, 2)
    def test_get_init(self):
        self.assertEqual(self._width, 3)
    
    def test_get_mass(self):
        self.assertEqual(r.mass(), 28)
    def test_get_volume(self):
        self.assertEqual(r.MassCount(), 168)

if __name__ == '__main__':
    unittest.main()

