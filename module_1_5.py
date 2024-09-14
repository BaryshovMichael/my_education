immutable_var = (1,1.5,'kitten')
print ('Immutable tuple:', immutable_var)
#эллементы кортежа нельзя изменить или редкатировать, т.к. кортеж не поддерживает обращение по элементам
mustable_list = ['баклажан', 'помидор', 'морковка']
mustable_list[1] = 'сельдерей'
mustable_list.extend([21, 3.5])
print ('Mutable list:', mustable_list)
