# Вариант 4

file = open("books-en.csv")
column_names = file.readline() #строчка с названиями колонок
count = 0
data = [x[:-1] for x in file]


GREEN = '\033[32m'
RED = '\033[31m'
END = '\033[0m'


for i in range(len(data)):
    data[i] = data[i].split(';')


# Задание 1
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