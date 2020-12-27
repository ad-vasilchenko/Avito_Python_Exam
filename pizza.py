from utils import *
from ingridients import *
from random import randint


class Pizza:
    def __init__(self):
        pass

    @time_report("Начали готовить пиццу", "Пицца приготовлена за {} мин.")
    def bake(self):
        """
        Здесь мы готовим пиццу
        """

        t = randint(1, 2)
        time.sleep(t)

    @time_report("Курьер забрал пиццу", "Пицца доставлена за {} мин.")
    def delivery(self):
        """
        Здесь мы доставляем пиццу
        """

        t = randint(1, 2)
        time.sleep(t)

    def __str__(self):
        return f'{self.name} : {", ".join(map(str, self.ingridients))}'


class Margarita(Pizza):
    name = "Margarita"
    ingridients = [Tomatoes(weight=20), Cheese(weight=10)]


class Pepperony(Pizza):
    name = "Pepperony"
    ingridients = [Tomatoes(weight=20), Tomato_Sauce(weight=10), Meat(weight=50)]
