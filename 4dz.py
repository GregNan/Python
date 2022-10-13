# # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# # my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
# #     этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# # def del_some_words(my_text):
# #     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
# #     return " ".join(my_text)

# # my_text = del_some_words(my_text)
# # print(my_text)

# # # Создайте программу для игры с конфетами человек против человека.

# # # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# # #  За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# # import random

# # greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
# #     'Основные правила игры: '
# #     'Нам будет дано некоторое количество конфет, '
# #     'за один ход мы можем взять не более определённого количества, '
# #     'о котором мы с вами договоримся.'
# #     'Итак, начнём!')
            

# # messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
# #             'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


# # def play_game(n, m, players, messages):
# #     count = 0
# #     if n%10 == 1 and 9 > n > 10: letter = 'а'
# #     elif 1 < n%10 < 5 and 9 > n > 10: letter = 'ы'
# #     else: letter = ''
# #     while n > 0:
# #         print(f'{players[count%2]}, {random.choice(messages)}')
# #         move = int(input())
# #         if move > n or move > m:
# #             print(f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
# #             attempt = 3
# #             while attempt > 0:
# #                 if n >= move <= m:
# #                     break
# #                 print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
# #                 move = int(input())
# #                 attempt -=1
# #             else: 
# #                 return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
# #         n = n - move
# #         if n > 0: print(f'Осталось {n} конфет{letter}')
# #         else: print('Все конфеты разобраны.')
# #         count +=1
# #     return players[not count%2]

# # print(greeting)

# # player1 = input('Давайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
# # player2 = input('Второй игрок, и Вы представьтесь, пожалуйста\n')
# # players = [player1, player2]

# # n =  2021
# # # int(input('Сколько конфет будем разыгрывать?\n '))
# # m = 28 
# # # int(input('Сколько максимально будем брать конфет за один ход?\n '))

# # winer = play_game(n, m, players, messages)
# # if not winer:
# #     print('У нас нет победителя.')
# # else: print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')
# # # a) Добавьте игру против бота
# # from random import randint, choice

# # greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
# #             'Основные правила игры: '
# #             'Нам будет дано некоторое количество конфет, '
# #             'за один ход мы можем взять не более определённого количества, '
# #             'о котором мы с вами договоримся. '
# #             'Итак, начнём!')

# # messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
# #             'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


# # def introduce_players():
# #     player1 = input('Давайте познакомися. Как Вас зовут?\n')
# #     player2 = 'Робик'
# #         print(f'Очень приятно, меня зовут {player2}')
# #     return [player1, player2]


# # def get_rules(players):
# #     n = int(input('Сколько конфет будем разыгрывать?\n '))
# #     m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
# #     first = int(input(
# #         f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
# #     if first != 1:
# #         first = 0
# #     return [n, m, int(first)]


# # def play_game(rules, players, messages):
# #     count = rules[2]
# #     if rules[0] % 10 == 1 and 9 > rules[0] > 10:
# #         letter = 'а'
# #     elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
# #         letter = 'ы'
# #     else:
# #         letter = ''
# #     while rules[0] > 0:
# #         if not count % 2:
# #             move = randint(1, rules[1])
# #             print(f'Я забираю {move}')
# #         else:
# #             print(f'{players[0]}, {choice(messages)}')
# #             move = int(input())
# #             if move > rules[0] or move > rules[1]:
# #                 print(
# #                     f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
# #                 attempt = 3
# #                 while attempt > 0:
# #                     if rules[0] >= move <= rules[1]:
# #                         break
# #                     print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
# #                     move = int(input())
# #                     attempt -= 1
# #                 else:
# #                     return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
# #         rules[0] = rules[0] - move
# #         if rules[0] > 0:
# #             print(f'Осталось {rules[0]} конфет{letter}')
# #         else:
# #             print('Все конфеты разобраны.')
# #         count += 1
# #     return players[count % 2]


# # print(greeting)

# # players = introduce_players()
# # rules = get_rules(players)

# # winer = play_game(rules, players, messages)
# # if not winer:
# #     print('У нас нет победителя.')
# # else:
# #     print(
# #         f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')

# # # b) Подумайте как наделить бота ""интеллектом""
# # from random import randint, choice

# # greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
# #             'Основные правила игры: '
# #             'Нам будет дано некоторое количество конфет, '
# #             'за один ход мы можем взять не более определённого количества, '
# #             'о котором мы с вами договоримся. '
# #             'Итак, начнём!')

# # messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
# #             'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


# # def introduce_players():
# #     player1 = input('Давайте познакомися. Как Вас зовут?\n')
# #     player2 = 'Робик'
# #     print(f'Очень приятно, меня зовут {player2}')
# #     return [player1, player2]


# # def get_rules(players):
# #     n = int(input('Сколько конфет будем разыгрывать?\n '))
# #     m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
# #     first = int(input(
# #         f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
# #     if first != 1:
# #         first = 0
# #     return [n, m, int(first)]


# # def play_game(rules, players, messages):
# #     count = rules[2]
# #     print(count)
# #     if rules[0] % 10 == 1 and 9 > rules[0] > 10:
# #         letter = 'а'
# #     elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
# #         letter = 'ы'
# #     else:
# #         letter = ''
# #     while rules[0] > 0:
# #         if not count % 2:
# #             move = rules[0] % rules[1] + 1
# #             print(f'Я забираю {move}')
# #         else:
# #             print(f'{players[0]}, {choice(messages)}')
# #             move = int(input())
# #             if move > rules[0] or move > rules[1]:
# #                 print(
# #                     f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
# #                 attempt = 3
# #                 while attempt > 0:
# #                     if rules[0] >= move <= rules[1]:
# #                         break
# #                     print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
# #                     move = int(input())
# #                     attempt -= 1
# #                 else:
# #                     return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
# #         rules[0] = rules[0] - move
# #         if rules[0] > 0:
# #             print(f'Осталось {rules[0]} конфет{letter}')
# #         else:
# #             print('Все конфеты разобраны.')
# #         count += 1
# #     return players[not count % 2]


# # print(greeting)

# # players = introduce_players()
# # rules = get_rules(players)

# # winer = play_game(rules, players, messages)
# # if not winer:
# #     print('У нас нет победителя.')
# # else:
# #     print(
# #         f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')

# Создайте программу для игры в ""Крестики-нолики"".
def mytic(val):
    print("\n")
    print("\t    |   |")
    print("\t  {}  | {}   | {}".format(val[0], val[1], val[2]))
    print('\t____|____|____')

    print("\t    |   |")
    print("\t  {}  | {}   | {}".format(val[3], val[4], val[5]))
    print('\t____|____|____')
    
    print("\t    |   |")
    print("\t  {}  | {}   | {}".format(val[6], val[7], val[8]))
    print('\t____|____|____')
    print("\n")
def singlegame(curplayer):
    val = ['' for i in range(9)]
    playerpos = {'X' : [], 'O' : []}
while True:
    mytictactoe(val)
try:
    print("Player", curplayer, "turn. Choose your Block:", end="")
    chance = int(input())
except ValueError:
    print("Invalid Input! Try Again")
    continue

if chance < 1 or chance > 9:
    print("Invalid Input! Try Again")
    continue
if val[chance - 1] != ' ':
    print("Mesto zanyito.TA!")
    continue
val[chance -1] = curplayer
playerpos[curplayer].append(chance)

if check_Victory(playerpos, curplayer):
    mytic(val)
    print("pozdravlenie", curplayer, "pobeda")
    print("\n")
    return curplayer

if check_Tie(playerpos):
    mytic(val)
    print("Proigral")
    print("\n")
    return 'D'

def check_Victory(playerpos, curplayer):
    solution = [[1, 2, 3], [4, 5, 6],[7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in solution:
        if all(j in playerpos[curplayer] for j in i):
            return True
        return False
def check_Tie(playerpos):
    if len(playerpos['X']) + len(playerpos['O']) ==9:
        return True
    return False
if curplayer == 'X':
    curplayer = 'O'
else:
    curplayer = 'X'
if __name__ == "__main__":
    print("First Player")
    FirstPlayer = input("Specify the Name:")
    print("vtor igrok")
    SecondPlayer = input("Specify the Name:")
    print("\n")

curplayer = FirstPlayer
playerchoice = {'X': "", 'O' : ""}
opt = ['X', 'O']
scoreboard = {FirstPlayer: 0, SecondPlayer: 0}
myscoreboard(scoreboard)
def myscoreboard(scoreboard):
    print("\t---------------------------")
    print("\t           score board     ")
    print("\t---------------------------")

    listofplayers = list(scoreboard.keys())
    print("\t ", listofplayers[0], "\t  ", scoreboard[listofplayers[0]])
    print("\t ", listofplayers[1], "\t  ", scoreboard[listofplayers[1]])

    print("\t------------------------\n")

while True:
    print(curplayer, "will make the choice:")
    print("Press 1 for X")
    print("Press 2 for O")
    print("Press 3 to Quit")

try:
    the_choice = int(input())
    # except ValueError:
    # print("Invalid input!!! Try again\n")
    # continue

    if the_choice == 1:
        playerchoice['X'] = curplayer
        if curplayer == FirstPlayer:
            playerchoice['O'] = SecondPlayer
        else:
            playerchoice['O'] = FirstPlayer

    elif the_choice == 2:
        playerchoice['O'] = curplayer
        if curplayer == FirstPlayer:
            playerchoice['X'] = SecondPlayer
        else:
            playerchoice['X'] = FirstPlayer

    elif the_choice == 3:
        print("The Final Scores")
        myscoreboard(scoreboard)
        break

    else:
        print("oshibka! poprob snova")

    win = singlegame(opt[the_choice - 1])

    if win != "D" :
        playerWon = playerchoice[win]
        scoreboard[playerWon] = scoreboard[playerWon] + 1

    myscoreboard(scoreboard)

    if curplayer == FirstPlayer:
        curplayer = SecondPlayer
    else:
        curplayer = FirstPlayer









# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # Входные и выходные данные хранятся в отдельных текстовых файлах.
# with open('4dz.txt', 'r') as data:
#     my_text = data.read()

# def encode_rle(ss):
#     str_code = ''
#     prev_char = ''
#     count = 1
#     for char in ss:
#         if char != prev_char:
#             if prev_char:
#                 str_code += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     return str_code

            
# str_code = encode_rle(my_text)
# print(str_code)

# with open('4dz1.txt', 'r') as data:
#     my_text2 = data.read()

# def decoding_rle(ss:str):
#     count = ''
#     str_decode = ''
#     for char in ss:
#         if char.isdigit():
#             count += char 
#         else:
#             str_decode += char * int(count)
#             count = ''
#     return str_decode

# str_decode = decoding_rle(my_text2)
# print(str_decode)