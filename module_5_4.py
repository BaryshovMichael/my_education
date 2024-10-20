
class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors): # инициализация
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor):
        floor = 0
        if new_floor > self.number_of_floors or new_floor < 1: # условие проверки этажности
            print('Такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor+1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
         return self.number_of_floors <= other.number_of_floors


    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
         return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors is True


    def __add__(self, value):   # увеличивает кол-во этажей на переданное значение value, возвращает сам объект self
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
            return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

    def __del__(self):
        print(self.name, 'снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
