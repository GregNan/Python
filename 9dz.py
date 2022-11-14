# Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ
class NonNegative:
    def __init__(self, my_attr):
        self.my_attr = my_attr
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value
    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

class Worker:
    hours = NonNegative('hours')
    rate = NonNegative('rate')
    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate

    def total_profit(self):
        return self.hours * self.rate
OBJ = Worker('Иван', 'Иванов', 10, 100)
print(OBJ.total_profit())
OBJ.hours = 10
OBJ.rate = 100
print(OBJ.__dict__)
print(OBJ.total_profit())
del OBJ.rate
print(OBJ.__dict__)
OBJ = Worker('Иван', 'Иванов', 10, 100)
print(OBJ.total_profit())
OBJ.hours = 10
OBJ.rate = 100
print(OBJ.total_profit())

# # Создать метакласс для паттерна Синглтон (см. конец вебинара)
# AGE = 35
# print(AGE.__class__.__class__)
# NAME = 'Иван'
# print(NAME.__class__)

# def my_func():
#     pass

# print(my_func.__class__)

# class MyClass:
#     pass
# MC = MyClass()
# print(MC.__class__)

# print(AGE.__class__.__class__)
# print(NAME.__class__.__class__)
# print(my_func.__class__.__class__)
# print(MC.__class__.__class__.__class__)

# class DocMeta(type):
#     def __init__(self, clsname, bases, clsdict):
#         for key, value in clsdict.items():
#             if key.startswith("__"):
#                 continue

#             if not hasattr(value, "__call__")
#                 continue
#             if not getattr(value, "__doc__"):
#                 raise TypeError(f"Метод {key} должен иметь строку документации")
#         type.__init__(self, clsname, bases, clsdict)

# class MyClass(metaclass=DocMeta):
#     def method_1(self):
#         pass
#     def method_2(self):
#         "!"
#         print("Небольшая проблема")
# mc = MyClass()
# print(MyClass.__dict__)

# class MyClass():
#     pass
# obj_1 = MyClass()
# obj_2 = MyClass()
# obj_3 = MyClass()
# obj_4 = MyClass()
# print(obj_4)