# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def fib(n):
    if (n == 0):
         return 0 
    elif(n in [1,2]):
        return 1   
    else: 
        return (fib(n-1) + fib(n- 2))

el = int(input('k = '))    
num = []
num_sm = []
null = [0]
for i in range(1, el + 1):
    val = fib(i)
    val_sm = fib(i) * (-1) ** (i + 1)
    num.append(val)
    num_sm.append(val_sm)
    num_sm_rev = list(reversed(num_sm))

print(num_sm_rev + null + num)






