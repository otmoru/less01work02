month = int(input('Введите порядковый номер месяца от 1 до 12: '))
seasons = ['зима', 'весна', 'лето', 'осень']
if month < 3 or month > 11:
    print(seasons[0])
elif 6 > month > 2:
    print(seasons[1])
elif 9 > month > 5:
    print(seasons[2])
elif 12 > month > 8:
    print(seasons[3])