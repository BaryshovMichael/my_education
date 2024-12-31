from pprint import pprint

def  custom_write(file_name, strings):
    file = open (file_name, 'w', encoding='utf-8')
    string_position = { }
    str_num = 0
    str_start_byte = file.seek(0)
    for string_ in strings:
        file.write(string_+'\n')
        str_num += 1
        key = (str_num, str_start_byte)
        string_position[key]= string_
        str_start_byte = file.tell()
    file.close()
    return string_position

file_name = 'text.txt'
strings = ['Если б было море пива', 'я б дельфином стал красивым',
           'Если б было море водки', 'я бы стал подводной лодкой']
result = custom_write(file_name, strings)
pprint(result)