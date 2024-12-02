# Ввод: строки программы
#       признаком остановки является пустая строка
# Вывод: строка, очищенная от комментариев
string = input()
while (string != ''):
    comment = string.find('#')
    if string.strip().startswith('#'):
        string = input()
        continue
    elif comment == -1:
        print(string)
    else:
        print(string[:comment])
    string = input()
# # Мой первый цикл
# for i in range(10): # Считаем до 10
#     print(i) # выводим число

# for i in range(10):
#     print(i)