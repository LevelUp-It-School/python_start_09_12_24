#Управление кафе:

#1. класс Drink: name, volume; display_info

class Drink:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
    
    def display_info(self):
        print(f"{self.name} - {self.volume} мл.")

class HotDrink(Drink):
    def __init__(self, name, volume, temperature=75):
        super().__init__(name, volume)
        self.temperature = temperature
    def display_info(self):
        print(f"{self.name} - {self.volume} мл., температура: {self.temperature} C")

class ColdDrink(Drink):
    def __init__(self, name, volume, ice_cubes=3):
        super().__init__(name, volume)
        self.ice_cubes = ice_cubes
    def display_info(self):
        print(f"{self.name} - {self.volume} мл., кубики льда: {self.ice_cubes}")

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def order_drink(self, drink):
        self.orders.append(drink)
        print(f"{self.name} заказал: {drink.name}")

    def show_order(self):
        print(f"Заказы {self.name}: ")
        for drink in self.orders:
            drink.display_info()

class DrinkMenu:
    def __init__(self):
        self.drinks = []
    
    def add_drink(self, drink):
        self.drinks.append(drink)
        print(f"{drink.name} добавлен в меню")

    def show_all_drinks(self):
        print("Меню напитков:")
        for i in self.drinks:
            i.display_info()


cocoa = Drink("Какао", 330)
cocoa.display_info()
tea = HotDrink('черный чай', 200, 100)
tea.display_info()
cola = ColdDrink("кола", 500, 5)
cola.display_info()

customer = Customer("Иван")
customer.order_drink(cocoa)
customer.order_drink(tea)
customer.show_order()

menu = DrinkMenu()
menu.add_drink(cocoa)
menu.add_drink(tea)
menu.add_drink(cola)
menu.show_all_drinks()