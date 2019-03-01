"""
    Store Class
"""


class Store:
    def __init__(self, inventory):
        self.inventory = inventory
        self.active_rentals = []
        self.completed_rentals = []

    def rent_tool(self, customer, n_nights, n_tools, category):
        if not self.inventory.is_valid_request(n_tools, category) or not customer.is_valid_request(n_tools, n_nights):
            return -1, []
        self._rent_tools(n_tools, category, customer)

    def _rent_tools(self, n_tools, category, customer):
        rented_tools = self.inventory.rent_tools(category, n_tools)


class Rental:
    def __init__(self, customer, rental_day, day_of_return):
        self.customer = customer
