#0. Вывести квадрат числа
#number = int(input('Введите число \n'))
#print('Квадрат числа {} равен {}'.format(number, number**2))
#print(f'Квадрат числа {number} равен {number**2}')
#print('Квадрат числа', number, 'равен', number**2)
#2 принимает 5 чисел и находит максимальное из них
#list = [1,4,8,7,50]
#max = list[0]
#for i in list:
#    if max < i:
#        max = i
#print (f"Максимальное число равно {max}")
#3 Вход N и воводит числа от -N до N
#n = abs(int(input("N=")))
#for i in range(-n,n+1):
#    print(i,end='')
#    print('\n')
#4 на вход дробь и показывает первую цифру дробной части
#a = float(input("Введите дробное число с точкой"))
#n = int(a * 10 %10)
#print(n)
#5 кратно ли число 5,10,15 но не 30
#c = int(input("a ="))
#if ((c%5==0 and c%10==0) or c%15==0) and c%30!=0:
#    print('кратно число 5,10,15 но не 30')
#6. x V y V-or /\- and не1-not(1)
print('x y z f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = x or y or z
            print(x,y,z,bool(f))



