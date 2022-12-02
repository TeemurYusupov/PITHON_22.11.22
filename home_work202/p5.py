
import random
def mix_list(list1):            
    
    list = list1[:]
    
    for i in range(len(list)):
        index_el = random.randint(0, len(list) - 1)
  
        temp = list[i]                                
        list[i] = list[index_el]
        list[index_el] = temp
    return list

from random import randint
list = []
for i in range(10):
    list.append(randint (0,5))

mixed_list = mix_list(list)

print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)
