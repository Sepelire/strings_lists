food_menu = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
days_count = int(input())

for day in range(days_count):
    print(food_menu[day % len(food_menu)])