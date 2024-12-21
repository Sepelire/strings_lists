number_count = int(input())
number_arr = []
for i in range(number_count + 1):
    number_arr.append(int(input()))
power = number_arr[-1]
number_arr.pop()
for number in number_arr:
    print(number ** power)