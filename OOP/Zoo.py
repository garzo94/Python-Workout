class Sheep:
    number_of_legs = 4
    species = 'sheep'
    def __init__(self,color):
        self.color = color
    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'

class Wolves(Sheep):
    species = 'wolve'
    def __init__(self, color):
        super().__init__(color)

class Snakes(Sheep):
    species = 'snake'
    number_of_legs = 0
    def __init__(self, color):
        super().__init__(color)

class Parrots(Sheep):
    species = 'parrot'
    number_of_legs = 2
    def __init__(self, color):
        super().__init__(color)










