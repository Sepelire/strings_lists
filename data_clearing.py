# Ввод: строки
#       признаком завершения ввода считается пустая строка
# Вывод: очищенные данные

string = input()
while (string != ''):
    if string.endswith('@@@'):
        string = input()
        continue
    elif string.startswith('##'):
        right_string = string[2:]
        print(right_string)
    else:
        print(string)
    string = input()
# First Message
# ##Second Message
# @@@Third Message##
# ##Fourth Message@@@

# First Message
# Second Message
# @@@Third Message##