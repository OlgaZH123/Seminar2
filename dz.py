# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# import random


# def checking_the_input(n):
#     if n == 1:
#         print('Сколько не верти, лучше не станет!')
#     elif n == 0:
#         print('Может для начала разложим монеты?..')
#     elif n < 0:
#         print('Совсем что-ле?..')
#     else:
#         resource = get_array(n)
#         get_how_much_to_turn_over(resource)


# def get_array(n):
#     array = [random.choice(['O', 'R']) for _ in range(0, n)]
#     return array


# def get_how_much_to_turn_over(resource):
#     count = 0
#     temp = 0
#     for i in resource:
#         if i == 'R':
#             count += 1
#         else:
#             temp += 1
#     print(resource)
#     array = [count, temp]
#     if count == 0 or temp == 0:
#         print('Ничего не нужно переворачивать!')
#     elif count != temp:
#         print(f'Минимальное количество монет к перевороту: {min(array)}')
#     else:
#         print('Не важно какие переворачивать!')


# def main():
#     checking_the_input(n=int(input('Введите количество монет: ')))


# main()


# Задача 12
#  Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

import random
import math




def get_unknown_numbers():
    array = [random.randint(1, 1000) for _ in range(2)]
    # print(array)
    array_2 = [sum(array), math.prod(array)]
    return array_2


def get_numbers(numbers):
    x = 1
    while x * (numbers[0] - x) < numbers[1]:
        x += 1
    y = numbers[0] - x
    print(f'Числа загаданные Петей {x} и {y}')


def main():
    numbers = get_unknown_numbers()
    print('Сумма', numbers[0])
    print('Произведение', numbers[1])
    get_numbers(numbers)


if __name__ == '__main__':
    main()


# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
# превосходящие числа N.

# def get_pow_number(n):
#     array = [2 ** i for i in range(n)]
#     while array[-1] > n:
#         del array[len(array) - 1]
#     return array


# def main():
#     n = int(input('Введите натуральное число: '))
#     result = get_pow_number(n)
#     print(result)


# main()