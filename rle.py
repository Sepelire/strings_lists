# Ввод: Строка цифр длиной не меньше 1
# Вывод: Пары: сама цифра и количество повторений цифры подряд во введённой строке
number_string = input().strip()
current_num = number_string[0]
counter = 1

for number in number_string[1:]:
    if number == current_num:
        counter += 1
    else:
        print(current_num, counter)
        current_num = number
        counter = 1
print(current_num, counter)
# 010000100001111111110111110000000000000011111111

# 0 1
# 1 1
# 0 4
# 1 1
# 0 4
# 1 9
# 0 1
# 1 5
# 0 14
# 1 8