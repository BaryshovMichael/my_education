#Dictionary
my_dict = {'Petya': 1992, 'Olga': 1989, 'Vanya': 1990}
print('Dict:',my_dict)
print('Existing value:',my_dict['Olga'])
print('Not existing value:',my_dict.get('Pasha'))
my_dict.update ({'Tanya': 1991, 'Taras': 1994})
a=my_dict.pop('Vanya')
print ('Deleted value:',a)
print('Modified dictionary:',my_dict)

#Varietys
my_set = {123, 15.5, 'rock',123, False,555, 15.5, 16.1}
print('Set:',my_set)
my_set.update({133,17.2})
my_set.remove(123)
print('Modified set:', my_set)


