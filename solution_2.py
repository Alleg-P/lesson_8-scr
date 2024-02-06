# Задача 2: Синонимы в дизайне

synonyms = {'Красивый': 'Прекрасный', 
            'Уродливый': 'Некрасивый', 
            'Сложный': 'Запутанный', 
            'Простой': 'Лёгкий',
            'Полезный':'Необходимый',
            'Качественный': 'Добротный'}

while True:
    word = input('Введите слово: ')
    if word in synonyms.keys():
        print(f'Синоним Вашего слова {word}: ', synonyms[word])
    elif word in synonyms.values():
        antisynonyms = {value: key for key, value in synonyms.items()}
        print(f'Синоним Вашего слова {word}:', antisynonyms[word])
    else:
        print('Такого слова в словаре нет.')
    answer = input('Продолжить? Д/Н')
    if answer == 'Н':
        break
        