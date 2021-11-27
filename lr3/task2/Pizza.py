import json


class Pizza:
    information_about_pizza = []

    def __init__(self, day, pizza_name, price, *ingredients):
        self.day = day
        self.pizza_name = pizza_name
        self.price = price
        self.ingredients = ingredients
        Pizza.add_pizza_to_file(self)
        Pizza.add_ingredients_to_file()

    @staticmethod
    def add_ingredients_to_file():
        ingredients = ['mozzarella', 'chicken', 'tomato', 'mushrooms', 'pineapple',
                       'Dor Blue cheese', 'Gouda cheese', 'cream cheese', 'pepperoni',
                       'mozzarella', 'Italian herbs', 'bacon', 'ham', 'onions', 'olives',
                       'hunting sausages', 'salami', 'pickles', 'sauce', 'cheese', 'green', 'fish']
        with open('ingredients.json', 'w') as f:
            json.dump(ingredients, f)

    def add_pizza_to_file(self):
        pizza = {
            'Day': self.day,
            'Pizza name': self.pizza_name,
            'Price': self.price,
            'Ingredients': self.ingredients
        }
        Pizza.information_about_pizza.append(pizza)
        with open('pizza.json', 'w') as f:
            json.dump(Pizza.information_about_pizza, f)

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not isinstance(day, str):
            raise TypeError("Incorrect day type input")
        self.__day = day

    @property
    def pizza_name(self):
        return self.__pizza_name

    @pizza_name.setter
    def pizza_name(self, pizza_name):
        if not isinstance(pizza_name, str):
            raise TypeError("Incorrect name of pizza type input")
        self.__pizza_name = pizza_name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, str):
            raise TypeError("Incorrect price of pizza type input")
        if not price > 0:
            raise ValueError("Incorrect price of pizza value input")
        self.__price = price

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        if any(not isinstance(value, str) for value in ingredients):
            raise TypeError("Incorrect ingredients type input")

        with open("ingredients.json", "r") as f:
            data = json.load(f)
        for item in ingredients:
            if item not in data:
                raise ValueError("This ingredient cannot be added")
        self.__ingredients = list(ingredients)

    def __str__(self):
        return f"{self.__day} pizza: {self.__pizza_name}\nPrice: {self.__price}\nIngredients: {self.__ingredients}"


class MondayPizza(Pizza):

    def __init__(self, *args):
        super().__init__('Monday', 'Hawaiian', 150, 'chicken', 'pineapple', 'mushrooms', 'mozzarella', 'sauce', *args)


class TuesdayPizza(Pizza):

    def __init__(self, *args):
        super().__init__('Tuesday', 'Four cheeses', 125, 'chicken', 'pineapple', 'mushrooms', 'mozzarella',
                         'sauce', *args)


class WednesdayPizza(Pizza):

    def __init__(self, *args):
        super().__init__('Wednesday', 'Margarita', 90, 'tomato', 'mozzarella', 'sauce', *args)


class ThursdayPizza(Pizza):

    def __init__(self, *args):
        super().__init__('Thursday', 'Pepperoni', 120, 'pepperoni', 'mozzarella', 'Italian herbs', 'sauce', *args)


class FridayPizza(Pizza):

    def __init__(self, *args):
        super().__init__('Friday', 'Carbonara', 170, 'bacon', 'ham', 'mushrooms', 'onions', 'olives', 'mozzarella',
                         'sauce', *args)


class SaturdayPizza(Pizza):

    def __init__(self, *args):
        super().__init__('Saturday', 'Hunting', 130, 'hunting sausages', 'salami', 'pickles', 'onions', 'mozzarella',
                         'sauce', *args)


class SundayPizza(Pizza):

    def __init__(self, *args):
        super().__init__('Sunday', 'Branded', 100, 'chicken', 'salami', 'hunting sausages', 'mushrooms', 'mozzarella',
                         'sauce', *args)
