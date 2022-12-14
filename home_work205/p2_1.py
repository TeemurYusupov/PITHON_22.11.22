# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока 
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все 
# конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


from random import *
import os

def player_player():
    all_candies = 135
    max_take = 28
    count = 0
    
    player1 = input('\n Игрок 1 --> ')       #решаем кто есть кто
    player2 = input('\n Игрок 2 --> ')

    x = randint(1, 2)                       # жеребьевка
    if x == 1:
        first = player1
        secnd = player2
    else:
        first = player2
        secnd = player1
    print(f'{first} ты ходишь первым')

    while all_candies > 0:
        
        if count == 0:
            step = int(input(f'{first} твой ход:'))      # ход первого игрока
            
            if step > all_candies or step > max_take:
                step = int(input(f'{first} возьми меньше {max_take} конфет:  '))    #проверка лимита
            all_candies = all_candies - step
        
        if all_candies > 0:                                   #остаток
            print(f'осталось {all_candies} конфет')
            count = 1
        
        else:
            print('все конфеты кончились')

        if count == 1:
            step = int(input(f'{secnd} твой ход: '))          #ход второго игрока
            
            if step > all_candies or step > max_take:                              
                step = int(input(f'{secnd} возьми меньше {max_take} конфет: '))
            all_candies = all_candies - step
        
        if all_candies > 0:
            print(f'\nосталось {all_candies} конфет')
            count = 0
        
        else:
            print('все конфеты кончились')

    if count == 1:
        print(f'{secnd} победил!')
    if count == 0:
        print(f'{first} победил!')


player_player()