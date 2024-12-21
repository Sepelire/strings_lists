numbers = input()
numbers_arr = []
numbers_arr = numbers.split(" ")
power = int(input())

for number in numbers_arr:
    print(int(number) ** power, end=' ')