my_list = [7, 5, 3, 3, 2]
i = 0
print('Наш список ', my_list)
while i < 10:
    new = int(input('введите новый элемент для списка: '))
    my_list.append(new)
    print(my_list)
    my_list.sort()
    my_list.reverse()
    print(my_list)
    i += 1