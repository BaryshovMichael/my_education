def add_everything_up (a, b):

    try:
        result = a+b
    except TypeError as exc:
        print(f'действие невозможно, т.к. {exc}')
        return str(a)+str(b)
    else:
        return result
    finally:
        print('Мы всё равно произвели сложение во славу Омниссии!')


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))