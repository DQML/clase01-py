from Animal import Animal

class Dog(Animal):

    def __init__(self, name, age, size, color, race, id):
        
        super().__init__(name, age)
        self.size = size
        self.color = color
        self.race = race
        self.__id = id

    def printInfo(self):
        self.__Guau()
        print(self.getName(), self.getAge() self.size, self.color, self.race)

    def setId(self, id):
        if(id > 0):
          self.__id = id

    def __Guau(self):
        print("Guau, Guau !") 