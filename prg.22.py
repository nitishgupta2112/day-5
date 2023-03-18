class Customer:
    def __init__(self,quantity):
        self.__quantity = quantity

    def validate_quantity(self, quantity):
        if quantity>=1 and quantity<=5:
            return True
        else:
            return False
class PizzaService:
    counter = 100
    def validate_pizza_type(self,size):
        if size=="small" or size=="medium":
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if (self.validate_pizza_type()==True) and (self.validate_quantity()==True):
    