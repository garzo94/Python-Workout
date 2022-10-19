class Drink:
    count = 0 # static element

    def __init__(self,name):
        self.__name = name # encaptsulation
        Drink.count += 1
    def getDetail(self):
        return "la bebida es: " +self.__name

class Product:
    def __init__(self, cost, price):

        self.cost = cost
        self.price = price
    def getGain(self):
        return self.price -self.cost

class Beer(Drink,Product):
    def __init__(self,name,brand,alcohol, cost, price):
        Drink.__init__(self,name)
        Product.__init__(self,cost,price)
        self.__brand = brand
        self.__alcohol = alcohol
        self.cost = cost
    def getDetail(self):
        return super().getDetail() + "la marca es: " + self.__brand +" cost: " + str(self.cost)

beer1 = Beer(name='gALLO',cost=10,price=16,brand='Heey', alcohol=5.5)
# drink = Drink('gallo')
print(beer1.getDetail())
