# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков. Проанализировать результат и определить
# программы с наиболее эффективным использованием памяти.

import sys
# 1пример число  int 28 в системе os ubuntu  64 bit на python 3.9
# Сформировать из введенного числа обратное по порядку входящих в него цифр и
# вывести на экран. Например, если введено число 3486,
# то надо вывести число 6843.

# n = int(input('введите номер : '))
# """ приводим число к строке переворачиваем и возвращаем числовой формат"""
# reversed = int(str(n)[::-1])
# print(reversed)
# print(f' Размер равен: {sys.getsizeof(reversed)}')



# 2 пример  смотрим размер словаря(360) системе os ubuntu  64 bit на python 3.9
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из
# чисел в диапазоне от 2 до 9.
# div_dict = dict.fromkeys(range(2, 10), 0)
# for num in range(2, 100):
#     for i in range(2, 10):
#         if num % i == 0:
#             div_dict[i] += 1
#
# for key in div_dict:
#     print(f'{key} кратны {div_dict[key]} числам  ')
#
# print(f'размер  словаря равен: {sys.getsizeof(div_dict)}')

# 3 пример размер списков  системе os ubuntu  64 bit на python 3.9
import random

main_list = [random.randint(0, 100) for k in range(10)]
small_list = [k for k, item in enumerate(main_list) if item % 2 == 0]
print(f'Для массива: \n{main_list}\nИндексы четных элементов: \n{small_list}')
print(f' размер первоначального списка: {sys.getsizeof(main_list)}')
print(f' размер отформатированного списка: {sys.getsizeof(small_list)}')