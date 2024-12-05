max_count = 0
words_arr = []
list_string = []
string = ''
while True:
    word_for_array = input().lower().strip()
    if word_for_array == 'финиш':
        break
    words_arr.append(word_for_array)

string = ''.join(words_arr)
string_arr = string.split()
string = ''.join(string_arr)

list_string = list(string)
for letter in string:
    letter_count = list_string.count(letter)
    while letter in list_string:
        list_string.remove(letter)
    if max_count < letter_count:
        max_count = letter_count
        common_letter = letter
print(common_letter)