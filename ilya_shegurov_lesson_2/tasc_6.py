# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его
# отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться
# больше или меньше введенное пользователем число, чем то, что загадано. Если за 10
# попыток число не отгадано, то вывести загаданное число.
import random


number = random.randint(0, 100)
print(number)
user_number = None
count = 0
max_count = 10
while number != user_number:
    count += 1
    if count > max_count:
        print(f'загаданное число это {number}')
    print(f'попытка номер {count}')
    user_number = int(input('введите число'))
    """сравнение чисел"""
    if number < user_number:
        print('ваше число больше загаданного')
    elif number > user_number:
        print('ваше число меньше загаданного')


print('победа')
