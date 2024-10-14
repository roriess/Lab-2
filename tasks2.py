f=open("books-en.csv")
s=f.readline() #строчка с названиями колонок


a=[x[:-1] for x in f]
for i in range(len(a)):
    a[i]=a[i].split(';')


print("Укажите автора")
name=input()
for j in a:
    if j[2]==name:
        j[6]=j[6].replace(',','.')
        if float(j[6])<200:
            print("Доступна к скачиванию:")
            print("Название:",j[1])
            print("Автор:",j[2])
            print("Год публикации:",j[3])
            print("Опубликовано в:",j[4])
            print("Количество скачиваний:",j[5])
            print("Цена:",j[6])
            print("")
        else:
            print("Книга не доступна к покупке:")
            print("Название:",j[1])
            print("")