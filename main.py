first = int(input ('Введите первое число:'))
second = int(input('Введите второе число:'))
third = int(input('Введите третье число:'))

if first == second == third:
    print('Колличество одинаковых чисел:',3)
elif first == second or second == third or third == first:
    print('Колличество одинаковых чисел:',2)
else:
    print('Колличество одинаковых чисел:',0)