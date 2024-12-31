import  pprint
from string import punctuation

from module_7_2 import file_name

word = 'tExt'
class WordsFinder:
    res = { }
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = { }
        punctuation = ',.=!?;:'


        for filename in self.file_names:
            words = [ ]
            clear_line = ''
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    line =line.lower ()
                    while line.find(' - ') != -1:
                        line = line.replace(' - ', '')
                        continue
                    for char in line:
                        if not char in punctuation:
                            clear_line += char
                    words = clear_line.split()
                    all_words[filename] = words
                    self.res.clear()
                return all_words

    def find(self, word):  # - метод, где word - искомое слово.
        for names, words in self.get_all_words().items():
            place = 0
            if word.lower() in words:
                place = words.index(word.lower()) + 1
                self.res[names] = place
        return self.res

    def count(self, word):  # count(self, word) - метод, где word - искомое слово.
        for names, words in self.get_all_words().items():
            counter = 0
            if word.lower() in words:
                counter = words.count(word.lower())
                self.res[names] = counter
        return self.res

myfinder = WordsFinder('test_file.txt')
print(myfinder.get_all_words())
print(myfinder.find(word), f' # Позиция первого искомого слова "{word}" в списке:', *myfinder.res.values())
print(myfinder.count(word), f' # Количество повторений найденного слова "{word}": ', *myfinder.res.values(),'\n')