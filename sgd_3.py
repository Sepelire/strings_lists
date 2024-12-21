# Ввод: в единственной строке записывается последовательность натуральных чисел, разделённых пробелами
# Вывод: требуется вывести одно натуральное число — НОД всех данных чисел
numbers_str = input().split()
numbers_arr = []
for num_str in numbers_str:
    numbers_arr.append(int(num_str))
print(numbers_arr)

while len(numbers_arr) > 1:
    a = numbers_arr[0]
    b = numbers_arr[1]

    while b:
        a, b = b, a % b
    numbers_arr.pop(1)
    numbers_arr[0] = a
print(numbers_arr[0])
# 102 39 768

# 3