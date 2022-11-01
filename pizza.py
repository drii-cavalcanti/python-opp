class Pizza:

    size = 8

    def __init__(self, type) -> None:
        self.type = type
    
    def have_a_slice(self):
        self.size -= 1
    
    @classmethod
    def change_size(cls, size):
        cls.size = size
    
    @staticmethod
    def get_ingredients():
        return 'Base'

class Margherita(Pizza):

    @staticmethod
    def get_ingredients():
        return 'Tomate sauce, cheese and basil'

class Pepperoni(Pizza):
    ...

class HalfAndHalf(Margherita, Pepperoni):
    ...

class PizzaShop:
    def __init__(self) -> None:
        self._chef = Chef()

    def order(self, pizza):
        self._chef.make_pizza(pizza)

class Oven:
    def __init__(self) -> None:
        self.pizzas = []
        self.hardwoods = None
    
    def bake(self, pizza):
        if not self.hardwoods:
            print('No hardwoods')

class Chef:
    def __init__(self) -> None:
        self._oven = Oven()

    def make_pizza(self, pizza):
        self._oven.bake(pizza)