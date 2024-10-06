
def print_params(a =1, b= 'строка', c= True):
    print(a,b,c)


values_list = [3, 'ROCK', False]
values_dict = {'a': 5,'b': True,'c':'solomon'}

values_list_2 = [12.14, 'potato']

print_params()
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2,42)

