import os, time
from importlib.metadata import files

print('Текущая директория: ', os.getcwd())

directory = '.'
for root,dirs,files in os.walk(directory):
    for file in files:
        f=file
        filepath = os.path.join(root,f)
        filetime = os.path.getmtime(f)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(f)
        parent_dir = os.path.dirname(os.path.abspath(f))
        print(f'Обнаружен файл: {f}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
    break

