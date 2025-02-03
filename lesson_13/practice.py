# 1. Создать класс Animal: name, species
# 2. Создать подкласс Mammal: warm_blood = True; display_info и Bird: can_fly = True; display_info
# 3. Создать класс Zoo: animals = []; add_animal, show_all_animals

class Animal():
  def  __init__(self, name, species):
    self.name = name
    self.species = species

  def display_info(self):
      print(f"{self.name} - {self.species}")


class Mammal(Animal):
  def __init__(self, name, species, warm_blood = True):
    super().__init__(name, species)
    self.warm_blood = warm_blood

  def display_info(self):
    print(f"{self.name} - {self.volume}  {self.warm_blood}")


class Bird(Animal):
  def __init__(self, name, species, can_fly = True):
    super().__init__(name, species)
    self.can_fly = can_fly

  def display_info(self):
      print(f"{self.name} - {self.species} - {self.can_fly}")

class Zoo:
  def __init__(self):
    self.animals = []

  def add_animal(self, animals):
    self.animals.append(animals)

  def show_all_animals(self):
    for animal in self.animals:
        animal.display_info()

cow = Animal("Корова", "травоядное")
sokol = Bird("Сокол","птицы")
#zebra  = Mammal()  
zoo = Zoo()
zoo.add_animal(cow)
zoo.add_animal(sokol)
zoo.show_all_animals()