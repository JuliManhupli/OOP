
class Product:
    """
    Class Product
    This class stores information about a product
    It accepts 3 parameters:
    code, product, price
    """
    allCode = []

    def __init__(self, code, product, price):
        self.code = code
        self.name = product
        self.price = price

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        if not code:
            raise ValueError("Code is not specified")
        if not isinstance(code, int):
            raise TypeError("Incorrect code type")
        if code <= 0:
            raise ValueError("Incorrect code value")
        if code in self.allCode:
            raise ValueError("Duplicate code number")
        self.allCode.append(code)
        self.__code = code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, product):
        if not product:
            raise TypeError("Name product not specified")
        if not isinstance(product, str):
            raise TypeError("Incorrect name product type")
        self.__name = product

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

    def __str__(self):
        return f'Product {self.name}, code {self.code}, price {self.price}'


class Node:
    """
    Class Node
    This class stores information node of Binary Search Tree 
    It accepts 1 parameters: value of node
    """
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None


class Tree:
    """
    Class with Binary Search Tree
    """
    def __init__(self):
        self.__root = None

    def add(self, value):
        if not self.__root:
            self.__root = Node(value)
        else:
            Tree.__add(self.__root, value)

    @staticmethod
    def __add(node, value):
        if not isinstance(value, Product):
            raise TypeError("Incorrect type of insert!")
        if value.code < node.value.code:
            if node.left:
                return Tree.__add(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                return Tree.__add(node.right, value)
            else:
                node.right = Node(value)
        return True

    def show(self):
        Tree.__show(self.__root)

    @staticmethod
    def __show(node):
        if not node:
            return None
        Tree.__show(node.left)
        print(f"{node.value}")
        Tree.__show(node.right)

    def find(self, code):
        if not isinstance(code, int):
            raise TypeError('Incorrect code type')
        else:
            return self.__find(self.__root, code)

    @staticmethod
    def __find(node, code):
        if code < node.value.code:
            return Tree.__find(node.left, code)
        elif code > node.value.code:
            return Tree.__find(node.right, code)
        else:
            return node.value.price

    def all_cost(self, code, number):
        if not isinstance(code, int):
            raise TypeError('Incorrect code type')
        if not isinstance(number, int):
            raise TypeError('Incorrect number type')
        return self.find(code) * number


if __name__ == '__main__':
    o1 = Product(1, "First", 10)
    o2 = Product(2, "Second", 20)
    o3 = Product(3, "Third", 30)
    o4 = Product(4, "Fourth", 40)
    tree = Tree()
    tree.add(o1)
    tree.add(o2)
    tree.add(o3)
    tree.add(o4)
    tree.show()
    print(f"Five copies of the second product cost {tree.all_cost(2, 5)}")
