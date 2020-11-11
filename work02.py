new_list = []
resault_list = []
number = int(input("Введите длину списка: "))
while len(new_list) < number:
    new = input('введите значение для списка: ')
    new_list.append(new)
resault_list = new_list.copy()
print('Ваш список ',resault_list)
for index in range(len(new_list)):
    if number - 1 == index == 0:
        break
    if index % 2 == 0:
        if index < number - 1:
            resault_list[index] = new_list[index + 1]
        elif index == number - 1:
            break
    elif index % 2 != 0:
        resault_list[index] = new_list[index - 1]
print('Результат ',resault_list)




