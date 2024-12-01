# Ввод: натуральное число, количество слов
#       слова строчными буквами
# Вывод: YES — если все слова начинаются с нужной буквы
#        NO — если хотя бы одно слово начинается не с нужной буквы
raws_count = int(input())
flag = 'YES'
for i in range(raws_count):
    word = input()
    if word.startswith("а"):
        continue
    elif word.startswith("б"):
        continue
    elif word.startswith("в"):
        continue
    else:
        flag = 'NO'
print(flag)
# 3
# арбуз
# барабан
# ворона
# YES