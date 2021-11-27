from Order import *
from Pizza import *
from Customer import *

if __name__ == '__main__':
    o1 = MondayPizza('tomato')
    o2 = TuesdayPizza()
    o3 = WednesdayPizza('cheese')
    o4 = ThursdayPizza()
    o5 = FridayPizza()
    o6 = SaturdayPizza('fish')
    o7 = SundayPizza('cheese', 'green')

    c1 = Customer('First', 'Customer', '+380507004020')

    order1 = Order(c1, o4)
    print(order1)

    print(Order.get_pizza_of_day())