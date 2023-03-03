# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

n = int(input('Введите число: '))
rand_number = [random.randint(0, 100) for i in range(1, 10)]
print(rand_number)
temp = 0
closest_num = -1
for i in range(len(rand_number)):
    min_d = max(rand_number) - n
    if int(rand_number[i]) == n:
        temp += 1
for i in set(rand_number):
    if abs(i - n) < min_d:
        min_d = abs(i - n)
        closest_num = i
print(f' - {temp} раз встречается в заданном списке число {n},\n - максимально близкое число {closest_num} ')
