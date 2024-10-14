f=open("books-en.csv")
s=f.readline() #строчка с названиями колонок
count=0


a=[x[:-1] for x in f]
for i in range(len(a)):
    a[i]=a[i].split(';')


for j in a:
    if len(j[1])>30:
        count+=1
print(count)