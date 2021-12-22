#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.v

n = int(input())
change_mod = input('введите знак умножения * или сложения + : ')
digit_1 = n // 100
digit_2 = n // 10 % 10
digit_3 = n % 10
if change_mod == '+':
    print(f'Сумма чисел равна: {digit_1 + digit_2 + digit_3}')
if change_mod == '*':
    print(f'Произведение чисел равно :{digit_1 * digit_2 * digit_3}')


