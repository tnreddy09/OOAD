"""
    Store Class
"""


class Store:
    def __init__(self, inventory, customers):
        self.inventory = inventory
        self.active_rentals = []
        self.completed_rentals = []
        self.customer_list = customers
        self.amount = 0

    def rent_tool(self, customer, n_nights, tool_categories_map, day):
        if not self.inventory.is_valid_request(tool_categories_map) or\
                not customer.is_valid_request(tool_categories_map, n_nights):
            return -1, []
        self._rent_tools(tool_categories_map, customer, day, n_nights)

    def _calculate_price(self, tool_categories_map):
        price = 0
        for category, n_tools in tool_categories_map.items():
            price += self.inventory.get_section(category).get_price()
        return price

    def _rent_tools(self, tool_categories_map, customer, day, n_nights):
        rented_tools_map = self.inventory.rent_tools(tool_categories_map)
        n_tools = sum(tool_categories_map.values())
        price = self._calculate_price(tool_categories_map)
        rental = Rental(customer, day, day + n_nights, rented_tools_map,
                        price)
        self.amount += price
        rental.print_report("RENTED")
        customer.increase_active_rentals(n_tools)
        self.active_rentals.append(rental)

    def update_rentals(self, day):
        for rental_index in range(len(self.active_rentals)-1, -1, -1):
            if self.active_rentals[rental_index].day_of_return == day:
                rental = self.active_rentals.pop(rental_index)
                self.completed_rentals.append(rental)
                n_tools = rental.get_count_rented_items()
                rental.customer.decrease_active_rentals(n_tools)
                # update inventory with the returned items
                rental.print_report("RETURNED")
                self.inventory.return_tools(rental.rented_tools)

class Rental:
    def __init__(self, customer, rental_day, day_of_return, rented_tools_map, amount):
        self.customer = customer
        self.rental_day = rental_day
        self.day_of_return = day_of_return
        self.rented_tools = rented_tools_map
        self.amount = amount

    def print_report(self, rental_status):
        rented_items = "\n".join(["category: {}, number of tools: {}, tools: {}".format(cat, str(len(self.rented_tools[cat])), ", ".join(self.rented_tools[cat])) for cat in self.rented_tools])
        print("{} {} {} items on Day {} for {} nights".format(self.customer.name, rental_status,
                                                              self.get_count_rented_items(), self.rental_day,
                                                              self.day_of_return - self.rental_day))
        print("item information")
        print(rented_items)
        print("Cost for the Rental - $", self.amount)
        print("\n")

    def get_count_rented_items(self):
        return sum(len(self.rented_tools[cat]) for cat in self.rented_tools)
