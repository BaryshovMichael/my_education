from random import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self,_cords,speed):
        self._cords = [0,0,0]
        self.speed = speed

#move(self, dx, dy, dz), который должен менять соответствующие координаты в _cords на dx, dy и dz в том же порядке, где множителем будет являться speed. Если при попытке изменения координаты z в _cords значение будет меньше 0, то выводить сообщение "It's too deep, i can't dive :(" , при этом изменения не вносятся.
    def move(self,dx,dy,dz):
        dx = dx*self.speed
        dy = dy*self.speed
        dz = dz*self.speed# задать множители для скорости
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [dx, dy, dz]
            # if dz < 0 при dz умноженное на speed



    def get_cords(self):
        print(f'X:{self._cords()}')


    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")

        elif self._DEGREE_OF_DANGER > 5:
            print("Be careful, i'm attacking you 0_0" )


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        a = random.randint(1,4)
        print(f'Here are(is) {a} eggs for you')

class AquaticAnimal(Animal):

    def dive_in(self,dz):
        self._cords[2]-=abs((dz/2)*self.speed)

#dive_in(self, dz) - где dz изменение координаты z в _cords.
# Должен изменять в отрицательную сторону координату z уменьшенную в 2 раза с учётом скорости.
# С каким бы знаком не был передан параметр dz, внутри метода используйте его значение по модулю (функция abs).


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird,AquaticAnimal,PoisonousAnimal):
    def __init__(self,sound):
        sound = "Click-click-click"

db = Duckbill(10)

print(db.live)
print(db.beak)


db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()