# Ввод: натуральное число — количество чисел
#       в каждой из последующих строк записано по одному числу
#       в последней строке записано натуральное число — степень, в которую требуется возвести числа
number_count = int(input())
number_arr = []
for i in range(number_count + 1):
    number_arr.append(int(input()))
power = number_arr[-1]
number_arr.pop()
for number in number_arr:
    print(number ** power)
# 5
# 222222
# 22222
# 2222
# 222
# 22
# 2

# 49382617284
# 493817284
# 4937284
# 49284
# 484