class Car():
    def __init__(self,model: str,__vin: int,__numbers: str):
        self.model = model
        if self.__is_invalid_vin(__vin):
            self.__vin = __vin
        if self.__is_invalid_numbers(__numbers):
            self.__numbers = __numbers

    def __is_invalid_vin(self, vin_number):
        vin = vin_number
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номера (не число)')
        if not 1000000 <= vin <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True


    def __is_invalid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if not len(numbers) == 6:
            raise IncorrectCarNumbers('Неверная длина номера')

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')