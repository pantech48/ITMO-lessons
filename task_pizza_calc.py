class Ingredient:
    """Edible ingridients."""

    def __init__(self, name, weight, cost):
        self._name = name
        self._weight = weight
        self._cost = cost

    def get_name(self):
        """Return name of ingridient."""
        return self._name
    
    def get_weight(self):
        """Return weight of ingridient."""
        return self._weight

    def get_cost(self):
        """Return cost of ingridient."""
        return round(self._cost, 2)


class Pizza:
    """Creates object 'pizza'."""

    def __init__(self, name, weight=0, cost=0, ingridients=[]):
        self._name = name
        self._weight = weight 
        self._cost = cost
        self._ingridients = ingridients

    def get_name(self):
        """Return name of pizza."""
        return self._name

    def get_weight(self):
        """Return weight of pizza."""
        pizza_weight = 0

        for ingridient in self._ingridients:
            pizza_weight += ingridient.get_weight()

        return pizza_weight/1000
        
    def get_cost(self):
        """Return cost of pizza."""
        pizza_cost = 0

        for ingridient in self._ingridients:
            pizza_cost += ingridient.get_cost()

        return pizza_cost

    def add_ingredient(self, ingridient):
        """Take object 'ingredient' and add it into pizza."""
        self._ingridients.append(ingridient)

    
class Order:
    """Create object 'order'."""

    def __init__(self, weight=0, cost=0, orders=[]):
        self._orders = orders
        self._weight = weight
        self._cost = cost

    def add_pizza(self, pizza):
        """Take object 'pizza' and add it in order."""
        self._orders.append(pizza)

    def get_cost(self):
        """Return order cost in rubbles."""
        order_cost = 0

        for pizza in self._orders:
            order_cost += pizza.get_cost()

        return order_cost
    
    def print_receipt(self):
        """Print check on the screen."""
        for pizza in self._orders:
            print(f'{pizza.get_name()} ({pizza.get_weight():.3f}кг) - {pizza.get_cost():.2f}руб')







