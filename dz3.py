# Задача 16:
# import random


# def get_list():
#     n = int(input('введите длину списка: '))
#     numbers = [random.randint(1, n) for _ in range(n)]
#     return numbers


# def get_value(numbers, x):
#     value = f'встречается {numbers.count(x)} раз' if numbers.count(x) == 0 else f'не встречается'
#     print('\n' + f'В списке {numbers} элемент {x} ' + value)


# def main():
#     x = int(input('Введите искомое число: '))
#     get_value(get_list(), x)


# if __name__ == '__main__':
#     main()

# Задача 18:
# from random import randint


# def get_list():
#     n = int(input('введите длину списка: '))
#     numbers = sorted([randint(1, 1000) for _ in range(n)])
#     print(numbers)
#     return numbers


# def get_value(result, x):
#     text_result = f'Самым близким по величине элемент к заданному числу {x} является '
#     if x > result[-1]:
#         print(text_result, result[-1])
#         return
#     elif x < result[0]:
#         print(text_result, result[0])
#         return
#     else:
#         for i in range(len(result))[-2::-1]:
#             if x==result[i]:
#                 print(text_result, result[i])
#                 return
#             elif x > result[i]:
#                 if x-result[i]>result[i+1]-x:
#                     print(text_result, result[i+1])
#                     return
#                 elif x-result[i]==result[i+1]-x:
#                     print(text_result, result[i], 'и', result[i+1] )
#                     return
#                 else:
#                     print(text_result, result[i])
#                     return


# def main():
#     x = int(input('Введите искомое число: '))
#     result = get_list()
#     get_value(result, x)


# if __name__ == '__main__':
#     main()

# Задача 20:
def get_en_points():
    dictionary_en = {
        1: 'A' 'E' 'I' 'O' 'U' 'L' 'N' 'S' 'T' 'R',
        2: 'D' 'G',
        3: 'B' 'C' 'M' 'P',
        4: 'F' 'H' 'V' 'W' 'Y',
        5: 'K',
        8: 'J' 'X',
        10: 'Q' 'Z'
    }

    temp = []
    text = input('Enter the text: ')
    print('The resulting value:', text)
    text = text.upper()
    for i in text:
        temp += [keys for keys, value in dictionary_en.items() if i in value]
    print(f'Вы набрали {sum(temp)} очков')


def get_ru_points():
    dictionary_ru = {
        1: 'А' 'В' 'Е' 'И' 'Н' 'О' 'Р' 'С' 'Т',
        2: 'Д' 'К' 'Л' 'М' 'П' 'У',
        3: 'Б' 'Г' 'Ё' 'Ь' 'Я',
        4: 'Й' 'Ы',
        5: 'Ж' 'З' 'Х' 'Ц' 'Ч',
        8: 'Ш' 'Э' 'Ю',
        10: 'Ф' 'Щ' 'Ъ'
    }

    temp = []
    text = input('Введите текст: ')
    print('Полученное значение: ', text)
    text = text.upper()
    for i in text:
        temp += [keys for keys, value in dictionary_ru.items() if i in value]
    print(f'Вы набрали {sum(temp)} очков')


def checking_the_input(language):
    language_ru = 'русский'
    language_en = 'english'
    if language.lower() == language_ru:
        get_ru_points()
    elif language.lower() == language_en:
        get_en_points()
    else:
        print('Введено неверное значение!')
        print('Invalid value entered!')


def main():
    language = input('Введите язык словаря (Enter the dictionary language): ')
    checking_the_input(language)


if __name__ == '__main__':
    main()