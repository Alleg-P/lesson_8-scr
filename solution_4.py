# Задача 4: Управление персоналом

supply = dict()  # Словарь для отдела снабжения (должность: фамилия)
design = dict()  # Словарь для отдела дизайна (должность: фамилия)

# Цикл набора сотрудников в отделы
for _ in range(6):
    department = input('Введите отдел: ')
    post = input('Введите должность: ')
    surname = input('Введите фамилию: ')
    if department == 'Снабжение':
        supply[post] = surname
    elif department == 'Дизайн':
        design[post] = surname
    else:
        print('Такого подразделения в штате нет.')
    print()
    
# Вывод штатного расписания
print('Снабжение:', supply)
print('Дизайн:', design)
