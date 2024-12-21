number_string = input().strip()
current_num = number_string[0]
counter = 1

for number in number_string[1:]:
    if number == current_num:
        counter += 1
    else:
        print(current_num, counter)
        current_num = number
        counter = 1
print(current_num, counter)