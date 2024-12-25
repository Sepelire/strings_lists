# Ввод: строки программы
#       признаком остановки является пустая строка
# Вывод: строка, очищенная от комментариев
strings_arr = []
while True:
    strings_arr.append(input())
    if strings_arr[-1] == '':
        break

for string in strings_arr[:-1]:
    comment = string.find('#')
    if string.strip().startswith('#'):
        continue
    elif comment == -1:
        print(string)
    else:
        print(string[:comment])
# # Мой первый цикл
# for i in range(10): # Считаем до 10
#     print(i) # выводим число

# for i in range(10):
#     print(i)