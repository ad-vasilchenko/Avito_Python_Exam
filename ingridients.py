class Ingridient:
    def __init__(self, weight):
        self.weight = weight

    def __str__(self):
        return str(self.name)


# Конечно, можно было бы не делать отдельный класс под каждый ингридиент.
# Но есть у меня ощущение, что в реальной пиццерии это был бы отдельный класс.
class Tomatoes(Ingridient):
    name = "tomatoes"


class Tomato_Sauce(Ingridient):
    name = "tomato saus"


class Meat(Ingridient):
    name = "meat"


class Cheese(Ingridient):
    name = "cheese"
