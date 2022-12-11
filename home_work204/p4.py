#  4. Задана натуральная степень k. Сформировать случайным образом
#  список коэффициентов (значения от 0 до 100) многочлена и записать
#   в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random
def write_file(st):
    with open('text_33.txt', 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0,10)

def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
def create_str(sp):
    lst= sp[::-1]
    writer = ''
    if len(lst) < 1:
        writer = 'x = 0'
    else:
        for i in range(len(lst)):
            
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                writer += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    writer += ' + '
            
            elif i == len(lst) - 2 and lst[i] != 0:
                writer += f'{lst[i]}x'
                if lst[i+1] != 0:
                    writer += ' + '
            
            elif i == len(lst) - 1 and lst[i] != 0:
                writer += f'{lst[i]} = 0'
            
            elif i == len(lst) - 1 and lst[i] == 0:
                writer += ' = 0'
    return writer

k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))
print(f"Занесли в файл данные: {create_str(koef)}")

