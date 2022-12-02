# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся 
# одной строкой, через пробел.

# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0
n = int(input('n = '))

# for item in range(-n, n + 1):
#    print(item, end=" ")

from random import randint
nums = []
for i in range(-n, n + 1):
    nums.append(randint (-n, n))
print(nums)
print()

x = int(input('элемент1--> '))
y = int(input('элемент 2--> '))
z = int(input('элемент3--> '))
print()

for i in range(len(nums)):
    rez = nums[x] * nums[y] * nums[z]
print('Вывод:', nums[x],'*', nums[y], '*', nums[z] ,'=', rez)