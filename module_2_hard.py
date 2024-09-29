import  random

def get_cipher():  # получим число первого поля
    numbers = list(range(3, 21))
    cipher = random.choice(numbers)
    return cipher



n = get_cipher()
print('Число   :', n)

pairnum1 = list(range(1, n))
pairnum2 = list(range(1, n))
pairs = []
result = ''

for i in pairnum1:
    for j in pairnum2:
        pn1 = i  #  pairnum1[i]
        pn2 = j  # pairnum2[j]
        if pn1 >= pn2:
            continue
        else:
            kratno = n % (pn1 + pn2)
            if kratno == 0:
                pairs.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)
print('Пары чисел', *pairs)
print('Пароль', result)
