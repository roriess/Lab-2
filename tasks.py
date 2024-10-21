from random import randint
import xml.etree.ElementTree as ET


# Вариант 4

file = open("books-en.csv")
column_names = file.readline() #строчка с названиями колонок
data = [x[:-1] for x in file]


GREEN = '\033[32m'
RED = '\033[31m'
END = '\033[0m'


for i in range(len(data)):
    data[i] = data[i].split(';')


# Задание 1
count = 0
for j in data:
    if len(j[1]) > 30:
        count += 1
print(f'Количество книг с длиной названия более 30: {count}')


# Задание 2
print("Укажите автора")
name = input()
for book in data:
    if book[2] == name:
        book[6] = book[6].replace(',','.')
        if float(book[6]) < 200:
            print(f'{GREEN} Доступна к скачиванию: {END} {book[1]}')
        else:
            print(f'{RED} Книга не доступна к покупке: {END} {book[1]}')


# Задание 3 
generator_result =  open('generator_result.txt','w')
numbers_of_book = len(data)
for i in range(1,21):
    number = randint(1,numbers_of_book)
    generator_result.write(f'{i} {data[number][2]}. {data[number][1]} - {data[number][3]} \n')


# Задание 4
file_currency = ET.parse('currency.xml')
currency_dictionary =  open('currency_dictionary.txt','w')
currency = file_currency.getroot()
for elem in currency:
   c=0
   for subelem in elem:
        c += 1
        if c == 1:
            currency_dictionary.write(f'NumCode: {subelem.text} ') 
        if c == 2:
            currency_dictionary.write(f'CharCode: {subelem.text} \n')
    
