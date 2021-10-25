import re


class Customer:
    """
    Class Customer
    It stores customer data
    Class takes 3 parameters of string type:
    name, surname and phone number of customer
    """
    def __init__(self, name, surname, phone):
        self.__name = name
        self.__surname = surname
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise TypeError("Name is not specified")
        if not isinstance(name, str):
            raise TypeError("Incorrect name type")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not surname:
            raise TypeError("Surname is not specified")
        if not isinstance(surname, str):
            raise TypeError("Incorrect surname type")
        self.__surname = surname

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Incorrect phone type")
        pattern = re.compile("^+380\\d{9}$")
        if not pattern.match(phone):
            raise ValueError("Wrong phone format")
        self.__phone = phone

    def __str__(self):
        return f"Name: {self.__name} {self.__surname}\nPhone: {self.__phone}"


class Product:
    """
    Class Product
    It stores product data
    Class takes 4 parameters:
    product name, description, price and dimension
    """

    def __init__(self, product, description, price, dimension):
        self.__nameProduct = product
        self.__description = description
        self.__price = price
        self.__dimension = dimension

    @property
    def name_product(self):
        return self.__nameProduct

    @name_product.setter
    def name_product(self, product):
        if not product:
            raise TypeError("Product name is not specified")
        if not isinstance(product, str):
            raise TypeError("Incorrect name product type")
        self.__nameProduct = product

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Incorrect description type")
        self.__description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, str):
            raise TypeError("Incorrect price type")
        if price <= 0:
            raise ValueError("Incorrect price value")
        self.__price = price

    @property
    def dimension(self):
        return self.__dimension

    @dimension.setter
    def dimension(self, dimension):
        if not isinstance(dimension, str):
            raise TypeError("Incorrect description type")
        self.__dimension = dimension

    def __str__(self):
        return f'Product {self.__nameProduct}, description {self.__description}, ' \
               f'price {self.__price}, dimensions = {self.__dimension}'


class Order:
    """
    Class Order
    It stores information about the order
    Class takes parameters about customer and some products selected by him
    Class has a method that calculates the total cost of order
    """
    def __init__(self, customer, *product):
        self.customer = customer
        self.products = product

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, value):
        self.__products = list(value)

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    def add_product(self, value):
        self.products.append(value)

    def del_product(self, value):
        self.products.remove(value)

    def get_sum_calculator(self):
        total = 0
        for item in self.products:
            total += item.price
        return str(total)

    def __str__(self):
        list_product = '\n'.join(list(map(str, self.products)))
        return f"Customer: \n{self.__customer}\nProducts: \n{list_product}"


if __name__ == '__main__':
    c1 = Customer("Ugly", "Duckling", "+3800502555213")
    o1 = Product("Apple", "Fruit", 25, "vog")
    o2 = Product("Tomato", "Vegetable", 4.15, "123")
    s = Order(c1, o1)
    s.add_product(o2)
    print(s)
    print("Order price " + s.get_sum_calculator())
