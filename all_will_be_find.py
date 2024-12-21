# Ввод: натуральное число — количество страниц, среди которых требуется произвести поиск
#       в каждой из последующих строк записаны заголовки страниц
#       в последней строке записан поисковый запрос
# Вывод: заголовки страниц, в которых присутствует поисковый запрос (регистр не имеет значения)
#        порядок заголовков должен сохраниться
raws_count = int(input()) + 1
raw_number = 0
i = 0
string_arr = []
lower_string_arr = []

for raw_number in range(raws_count):
    text = input()
    string_arr.append(text)
    lower_string_arr.append(text.lower())

query = lower_string_arr[-1]
string_arr.pop()
lower_string_arr.pop()

for lower_string in lower_string_arr:
    if query in lower_string:
        print(string_arr[i])
    i += 1
# 3
# Яндекс выпустил задачник по программированию
# На соревнованиях по программированию победил любитель питона
# Как заказать Яндекс.Такси?!
# яндекс

# Яндекс выпустил задачник по программированию
# Как заказать Яндекс.Такси?!