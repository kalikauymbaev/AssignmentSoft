# Base class for Pizza
class Pizza:
    def __init__(self):
        self.description = "Basic Pizza"
        self.price = 5.00  # base price for a Basic Pizza

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

# Decorator class that inherits from Pizza
class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_price(self):
        return self.pizza.get_price()

    def get_description(self):
        return self.pizza.get_description()

# Concrete decorator that adds Pepperoni topping
class PepperoniTopping(PizzaDecorator):
    def get_price(self):
        return self.pizza.get_price() + 2.00  # add $2.00 for Pepperoni topping

    def get_description(self):
        return self.pizza.get_description() + ", with Pepperoni"

# Concrete decorator that adds Mushroom topping
class MushroomTopping(PizzaDecorator):
    def get_price(self):
        return self.pizza.get_price() + 1.50  # add $1.50 for Mushroom topping

    def get_description(self):
        return self.pizza.get_description() + ", with Mushrooms"

# Testing the Decorator Pattern implementation
if __name__ == "__main__":
    # Start with a Basic Pizza
    basic_pizza = Pizza()
    print(basic_pizza.get_description(), "- Price:", basic_pizza.get_price())

    # Add Pepperoni topping
    pizza_with_pepperoni = PepperoniTopping(basic_pizza)
    print(pizza_with_pepperoni.get_description(), "- Price:", pizza_with_pepperoni.get_price())

    # Add Mushroom topping on top of Pepperoni
    pizza_with_pepperoni_and_mushrooms = MushroomTopping(pizza_with_pepperoni)
    print(pizza_with_pepperoni_and_mushrooms.get_description(), "- Price:", pizza_with_pepperoni_and_mushrooms.get_price())
