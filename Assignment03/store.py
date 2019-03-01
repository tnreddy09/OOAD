"""
    Store Class
"""


class Store:
    def __init__(self, inventory):
        self.inventory = inventory
        self.active_rentals = []
        self.completed_rentals = []

    def rent_tool(self, customer, n_nights, n_tools, category, day):
        if not self.inventory.is_valid_request(n_tools, category) or not customer.is_valid_request(n_tools, n_nights):
            return -1, []
        self._rent_tools(n_tools, category, customer, day, n_nights)

    def _rent_tools(self, n_tools, category, customer, day, n_nights):
        rented_tools = self.inventory.rent_tools(category, n_tools)
        price = self.inventory.get_section(category).get_price()

        rental = Rental(customer, day, day + n_nights, rented_tools, category, price * n_tools)
        self.active_rentals.append(rental)


class Rental:
    def __init__(self, customer, rental_day, day_of_return, tools, category, amount):
        self.customer = customer
        self.rental_day = rental_day
        self.day_of_return = day_of_return
        self.tools = tools
        self.category = category
        self.amount = amount
