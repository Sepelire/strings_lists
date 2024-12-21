# Ввод: натуральное число — длина строки
#       натуральное число — количество строк
#       строки
# Вывод: сокращённые строки
str_len = int(input())
raws_count = int(input())
for i in range(raws_count):
    string = input()
    if len(string) <= str_len:
        print(string)
    else:
        short_string = string[:str_len - 3] + '...'
        print(short_string)
# 25
# 3
# Начался саммит по глобальному потеплению
# Завтра Новый год!
# Python и Java конкурируют за звание самого популярного языка программирования
# Начался саммит по глоб...
# Завтра Новый год!
# Python и Java конкурир...