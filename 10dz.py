# Домашнее задание
# 1.	Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных. 
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.

# progr_1 = 'разработка'
# print(progr_1)
# progr_2 = 'сокет'
# print(progr_2)
# progr_3 = 'декоратор'
# print(progr_3)
# print(type(progr_1))
# print(type(progr_2))
# print(type(progr_3))




# 2.	Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов 
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
# bytes_1 = b'\xd0\xba\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81'
# bytes_2 = b'\xd1\x84\xd1\x83\xd0\xbd\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f'
# bytes_3 =b'\xd0\xbc\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb4'
# print(type(bytes_1))
# print(type(bytes_2))
# print(type(bytes_3))

# 3.	Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# 4.	Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
#  в байтовое и выполнить обратное преобразование (используя методы encode и decode).
#
# 5.	Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
# 6.	Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
#  Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
 progr_1 = 'разработка'
# print(progr_1)
# print(type(progr_1))
# print(ord('g'))
# bytes_s_1 = b'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'
# print(type(bytes_s_1))
# bytes_s_4 = b'Program'
# print(bytes_s_4)
# print(len(bytes_s_4))

# enc_str = 'разработка'
# enc_str_bytes = enc_str.encode('utf-8')
# print(enc_str_bytes)

# dec_str_bytes = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
# dec_str = dec_str_bytes.decode('utf-8')
# print(dec_str)

# import subprocess

# args = ['ping', 'google.com']
# subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
# for line in subproc_ping.stdout:
#     print(line)

# import telnetlib
# import time

# tn_connect = telnetlib.Telnet('10.0.0.1')

# tn_connect.read_until(b'Username:')
# tn_connect.write(b'user\n')

# t.read_until(b'Password:')
# t.write(b'pass\n')

# time.sleep(5)

# output = tn_connect.read_very_eager().decode('cp866').encode('utf-8')
# print(output.decode('utf-8'))	

# import locale

# def_coding = locale.getpreferredencoding()
# print(def_coding)

# f_n = open("test.txt", "w")
# f_n.write("test test test")
# f_n.close()
# print(f_n)

# err_str_1 = 'Программа'
# print(err_str_1.encode('ascii'))

# handl_err = 'Testování'
# handl_err_bytes = handl_err.encode('ascii', 'replace')
# print(handl_err_bytes)
# handl_err_bytes_2 = handl_err.encode('ascii', 'namereplace')
# print(handl_err_bytes_2)