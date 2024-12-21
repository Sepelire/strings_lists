string = input().lower().strip()
string_arr = []
reversed_string = []
for letter in string:
    if letter == ' ':
        continue
    else:
        string_arr.append(letter)
        reversed_string.insert(0, letter)
if string_arr == reversed_string:
    print('YES')
else:
    print('NO')