# Ввод: натуральное число — количество строк
#       строки
# Вывод: количество заек
raws_count = int(input())
bunnies_count = 0
for raw in range(raws_count):
    string = input()
    bunnies_count = string.count('зайка') + bunnies_count
print(bunnies_count)
# 3
# березка елочка зайка волк березка
# сосна зайка сосна елочка зайка медведь
# сосна сосна сосна белочка сосна белочка

# 3