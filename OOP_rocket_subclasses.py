from math import sqrt
from random import randint

class Rocket():
    '''Это класс ракеты с которым мы будем заниматься'''

    def __init__(self, x=0, y=0):
        
        self.x = x
        self.y = y

    def move_rocket(self, x_increment = 0, y_increment = 1):
        self.x += x_increment
        self.y += y_increment
    
    def get_distance(self, other_rocket):
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
class Shuttle(Rocket):

    def __init__(self, x=0, y=0, flights_completed = 0):
        super().__init__(x, y)
        #Rocket.__init__(self, x, y)
        self.flights_completed = flights_completed

# shuttle = Shuttle(10, 0, 3)
# print(shuttle)

shuttles = []
for x in range(3):
    x = randint(0, 100)
    y = randint(1, 100)
    flights_completed = randint(0,10)
    shuttles.append(Shuttle(x, y, flights_completed))    

rockets = []
for x in range(3):
    x = randint(0, 100)
    y = randint(1, 100)
    rockets.append(Rocket(x, y))    

for index, shuttle in enumerate(shuttles):
    print("Shuttle %d has %d flights." % (index, shuttle.flights_completed))

first_shuttle = shuttles[0]

for index, shuttle in enumerate(shuttles):
    distance = first_shuttle.get_distance(shuttle)
    print("The first shuttle is %.3f units away from shuttle %d" % (distance, index))

for index, rocket in enumerate(rockets):
    distance = first_shuttle.get_distance(rocket)
    print("The first shuttle is %.3f units away from rocket %d" % (distance, index))