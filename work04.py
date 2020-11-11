#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
#Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
new_list = input('ВВедите строку из нескольких слов разделенных пробелами: ')
my_list = new_list.split()
print(my_list)
sort = 0
while sort < len(my_list):
    if len(my_list[sort]) <= 10:
        print(sort+1, my_list[sort])
        sort += 1
    else:
        sort_list = list(my_list[sort])
        sort_list = sort_list[:10]
        s = ''
        my_list[sort] = s.join(sort_list)
        print(sort + 1, my_list[sort])
        sort += 1