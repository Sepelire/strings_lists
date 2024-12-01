# Ввод: строка
# Вывод: YES — если введенная строка является палиндромом, иначе – NO
string = input()
if string[0:] == string[-1::-1]:
    print('YES')
else:
    print('NO')
# мама
# NO