class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


pizza = Pizza(["Cheese", "tomato"])
print(pizza.pineapple_allowed)

pizza.pineapple_allowed = True