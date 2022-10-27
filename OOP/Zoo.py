import random

class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__ # this gives me a string reprentacion of the class
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species},{self.number_of_legs} legs'


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class Cage:
    cageID = random.randint(1,100)
    cage = []
    def add_animals(self, *args):
        for arg in args:
            self.cage.append(arg)
    def __repr__(self):
        return f'ID: {self.cageID}\n' + '\n'.join(animal.species for animal in self.cage)

class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self,*mycages):
        for cage in mycages:
            self.cages.append(cage)

    def animals_by_color(self,color):
        return [ animal for cage in self.cages for animal in cage if animal.color == color]

    def animals_by_legs(self, legs):
        return [animal for cage in self.cages for animal in cage if animal.number_of_legs == legs]

    def number_of_legs(self):
        return sum(animal.number_of_legs for cage in self.cages for animal in cage)






