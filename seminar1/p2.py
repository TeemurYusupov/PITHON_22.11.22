# 2. Напишите программу, которая на вход принимает 5 чисел
#  и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# num = 0
# maximum = 0

# for _ in range(5):
# num = int(input("Введите число: "))
# if num > maximum:
# maximum = num
# print(maximum)

from random import randint

numbers = []
for i in range(5):
   numbers.append(randint(-10, 10))
max_count = max(numbers)
print(numbers)
print(max_count)