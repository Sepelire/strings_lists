remaining_len = int(input()) - 3
string_count = int(input())
string_arr = []
current_len = 0
current_string = 0

for i in range(string_count):
    string_arr.append(input().strip())

for string in string_arr:
    current_string += 1
    if current_len + len(string) < remaining_len:
        print(string)
        current_len += len(string)
    else:
        if current_string == string_count:
            print(string)
        else:
            available_len = remaining_len - current_len
            print(string[:available_len] + '...')
            break

# 12
# 3
# 12345
# 1234
# 1234

# 12345
# 1234...