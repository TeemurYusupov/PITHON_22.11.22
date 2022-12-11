# 3. Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.
# 
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

import random

def list_1(n=10, min=5, max=20):
    list_nums = [random.randint(min, max)]
    for i in range (1, n):
        list_nums.append(random.randint(min, max)) 
    return list_nums


def unique_values_list(user_list):
    
    new_list = [user_list[0]]
    
    for i in range(1, len(user_list)):
        for j in range(len(new_list)):
            if user_list[i] == new_list[j]:
                del new_list[j]
            elif j == len(new_list)-1:
                new_list.append(user_list[i])
            
    return new_list

source_list = list_1(7, 5, 20)
unique_list = unique_values_list(source_list)
print(f'{source_list} ->')
print(unique_list)

