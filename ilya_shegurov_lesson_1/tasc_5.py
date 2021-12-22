#Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

char1 = input()
char2 = input()
num_char1 = ord(char1)
num_char2 = ord(char2)
dist = abs(num_char2 - num_char1)
print(f'Буква{char1}, {num_char1} числовой номер\n'
      f'Буква{char2}, {num_char2} числовой номер\n'
      f'Дистанция между буквами {dist}'
    )
