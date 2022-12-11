# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов
#  (складываются числа, у которых "х" в одинаковых степенях). 
#
#  Пример того, что будет в итогвом файле:  8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

with open('text1.txt', 'w') as file:
    file.write('8*(x**4) + 9*(x**3)')

with open('text2.txt', 'w', ) as file:
    file.write('1*(x**2) + 5*x + 4')

with open('text1.txt','r') as file:
    text1 = file.readline()
    lst_text1 = text1.split()

with open('text2.txt','r') as file:
    text2 = file.readline()
    lst_text2 = text2.split()

print(f'{lst_text1} + {lst_text2}')
text_sum = lst_text1 + lst_text2


with open('text_sum.txt', 'w') as file:
    file.write(f'{lst_text1} + {lst_text2} = 0')
