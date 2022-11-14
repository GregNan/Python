#  Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ
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
    seconds = NonNegative('seconds')
    
    def __init__(self, name, surname, seconds, rate):
        self.name = name
        self.surname = surname
        self.seconds = seconds
        self.rate = rate

    def total_profit(self):
        return self.seconds **2* self.rate
OBJ = Worker('Иван', 'Иванов', 10, 100)
print(OBJ.total_profit())
OBJ.seconds = 10
print(OBJ.total_profit())

# Создать метакласс для паттерна Синглтон (см. конец вебинара)
class Singleton(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs, **kwargs)
        cls.__instance = None
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance
class MySqlConnection(metaclass=Singleton):
    pass

sql_connection_1 = MySqlConnection()
sql_connection_2 = MySqlConnection()
a=3
print(a.__class__.__class__.__class__)