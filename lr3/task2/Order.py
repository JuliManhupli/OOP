from datetime import datetime
from Pizza import *
from Customer import *


class Order:
    information_about_orders = []

    def __init__(self, customer, pizza):
        self.customer = customer
        self.pizza = pizza
        Order.add_order_to_file(self)

    def add_order_to_file(self):
        order = {
            'Name': self.customer.name + ' ' + self.customer.surname,
            'Phone': self.customer.phone,
            'Pizza': self.pizza
        }
        Order.information_about_orders.append(order)
        with open('orders.json', 'w') as f:
            json.dump(Order.information_about_orders, f)

    @property
    def pizza(self):
        return self.__pizza

    @pizza.setter
    def pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError("That is not a Pizza type!")
        self.__pizza = pizza

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Incorrect customer type input")
        self.__customer = customer

    @staticmethod
    def get_pizza_of_day():
        day = datetime.now().strftime("%A")
        with open("pizza.json", "r") as file:
            data = json.load(file)
        for pizza in data:
            if pizza.get("Day") == day:
                return pizza

    def __str__(self):
        return f"Customer {self.customer}\nOrder:{self.pizza}\n\n"

