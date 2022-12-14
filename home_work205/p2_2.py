

from random import *
import os

def player_vs_bot():
    all_candies = 2021
    max_take = 28
    player1 = input('\nКак тебя зовут?: ')
    player2 = 'Компьютер'
    players = [player1, player2]
    
    first = randint(-1, 0)

    print(f'{players[first+1]} ты ходишь первым')

    while all_candies > 0:
        first += 1

        if players[first % 2] == 'Компьютер':
            print(f'\n \nосталось {all_candies}конфет\n ходит {players[first%2]}: ')

            if all_candies < 29:
                step = all_candies
            
            else:
                delenie = all_candies//28
                step = all_candies - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        
        else:
            step = int(input(f'\nНа кону {all_candies} конфет\n Ходит {players[first%2]}:  '))
            
            while step > max_take or step > all_candies:
                step = int(input(f'\nВозьми не более {max_take} конфет: '))
        all_candies = all_candies - step

    print(f'осталось {all_candies} \nПобедил {players[first%2]}')

player_vs_bot()
