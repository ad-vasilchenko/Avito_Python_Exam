from pizza import *
from operator import attrgetter


class Pizzeria:
    def __init__(self, pizza_list):
        self.pizza_list = pizza_list
        self.pizza_names = list(map(attrgetter("name"), pizza_list))

    def menu(self):
        for pizza in self.pizza_list:
            print(f"- {str(pizza)}")

    def order(self, pizza: str, delivery: bool):
        try:
            pizza_index = self.pizza_names.index(pizza)
        except:
            print("Такой пиццы нет в меню, сорян братишка")
            return

        pizza = self.pizza_list[pizza_index]
        pizza.bake()

        if delivery:
            pizza.delivery()
