# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв""

# text = input('введите текст: ')
text = 'Я люблю абвЖвау иабв Питон, Напишите программу, удаляющую из текста все слова, содержащие "абв".'

with open('file_888.txt', 'w', encoding='utf-8') as file:
    file.write(text)

def del_abv(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text_new = del_abv(text)
print(f'Сохранено: {text_new} "абв".')


with open('file_888.txt', 'a', encoding='utf-8') as file:
    file.writelines(text_new+' "абв".')