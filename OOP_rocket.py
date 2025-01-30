# class Rocket():
#     '''Это класс ракеты с которым мы будем заниматься'''

#     def __init__(self, x=0, y=0):
        
#         self.x = x
#         self.y = y

#     def move_up(self):

#         self.y += 1

# my_rocket = Rocket()
# print("Rocket altitude: ",  my_rocket.y)
# my_rocket.move_up()
# print("Rocket altitude: ",  my_rocket.y)
# my_rocket.move_up()
# print("Rocket altitude: ",  my_rocket.y)
# my_rocket.move_up()
# print("Rocket altitude: ",  my_rocket.y)


# rockets = []
# rockets.append(Rocket())
# rockets.append(Rocket(0, 10))
# rockets.append(Rocket(100, 0))

# for index, rocket in enumerate(rockets):
#     print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
from math import sqrt

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


# rockets = [Rocket() for x in range(3)]
# rockets[0].move_rocket()
# rockets[1].move_rocket(10, 10)
# for index, rocket in enumerate(rockets):
#     print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
rocket_1 = Rocket()
rocket_2 = Rocket(10, 5)

distance = rocket_1.get_distance(rocket_2)
print("The rockets are %f units apart." % distance)

