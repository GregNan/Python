# антипатерны
# (1+2)*3
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

# s = "(1+2)*3"
# result = parse(s)
# result = brackets(result)
# print(calc(result))
# print(parse("(1+2)*3"))


# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
# Формат: Объясняет преподаватель
# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **lambda, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.
# lambda, функция
# filter, 
# map, функция, список её реализация
# zip, кортежи из списков 
# enumerate, 
# list comprehension реализация функции в списке
# (1+2)*3

def parse(s):
    result = []
    digit = ''
    for symb in s: 
        if symb.isdigit():
            digit += symb
        elif symb in ['(',')']:
            if digit:
                result.append(float(digit))
                digit = ''
            result.append(symb)
        else:
            if digit:
                result.append(float(digit))
            digit = ''
            result.append(symb)
    else:
        if digit:
            result.append(float(digit))
    return result

def calc(lst):
    result = 0.0
    while '*' in lst:
        index = lst.index('*')
        lst = lst[:index - 1] + list(map((lambda result: lst[index-1] * lst[index+1]), lst[0])) + lst[index + 2:]
    while '/' in lst:
        index = lst.index('/')
        lst = lst[:index - 1] + list(map((lambda result: lst[index-1] / lst[index+1]), lst[0])) + lst[index + 2:]
    while '+' in lst:
        index = lst.index('+')
        lst = lst[:index - 1] + list[(map((lambda result: lst[index-1] + lst[index+1]), lst[0]))] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        lst = lst[:index - 1] + list(map((lambda result: lst[index-1] - lst[index+1]), lst[0])) + lst[index + 2:]
    return result
def brackets(lst):
    while '(' in lst:
        opening = lst.index('(')
        closing = lst.index(')')
        lst = lst[:opening] + [calc(lst[opening + 1:closing])] + lst[closing + 1:]
        return lst

s = "(1+2)*3"
result = parse(s)
print(result)
result = brackets(result)
print(result)
print(calc(result))
# print(parse("(1+2)*3"))

# lst = ['(', 1.0, '+', 2.0, ')', '*', 3.0]
# index = lst.index('+')
# result = lst[:index - 1] + [list(map((lambda result: lst[index-1] + lst[index+1]), lst[0]))] + lst[index + 2:]
# print(result)