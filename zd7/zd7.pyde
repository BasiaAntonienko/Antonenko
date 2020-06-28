from abc import ABCMeta, abstractmethod
class Pet():
     __metaclass__=ABCMeta
     @abstractmethod 
     def speak(self):
          abc().__init__()
          return 'no sound'
class Cat(Pet):
    def __init__(self, name):
         self.name = name
    def speak(self):
        text('Hau Hau', random(50, width-70), random(50, height-50))
        fill (0, 102, 153)
        return 'Hau Hau'
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('Miau Miau', random(30, width-100), random(30, height-60))
        fill (0, 255, 0)
        return 'Miau Miau'
    def mikusia(self):
        image(loadImage("mika.jpg.jpg"), random(50, width-70), random(50, height-100))
        tint (0,200, 255)
    def __add__(self, other): # miało być odejmowanie
        return self.name[0]+ ' i ' + other.name[0]
class GuineaPig(Pet):
    # tu miało być nadpisanie metody abstrakcyjnej
    pass
    
def setup():
    size(400,400)
    textSize(50)
    mika = Dog('Mika') #Mój pies
    czarek = Cat('Czarek') #Mój kot
    # a świnka?
    global list_of_pets
    list_of_pets = [mika, czarek]
    print(isinstance(czarek, Pet))
    print(mika)

def draw():
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak()
        if isinstance(pet, Dog):
             pet.mikusia()
# 0,75pkt
