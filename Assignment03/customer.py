"""
    Customer Information
"""
from random import randint

class Customer:
    def __init__(self, name, min_nights, max_nights, min_tools, max_tools):
        self.name = name
        self.min_nights = min_nights
        self.max_nights = max_nights
        self.min_tools = min_tools
        self.max_tools = max_tools
        self.active_rentals = 0


    def is_valid_request(self, tool_categories_map, n_nights):
        n_tools = sum(tool_categories_map.values())
        if (self.min_nights <= n_nights <= self.max_nights) and \
                (self.min_tools <= n_tools <= self.max_tools) and (self.active_rentals + n_tools <= 3):
            return True
        return False

    def increase_active_rentals(self, n_tools):
        self.active_rentals += n_tools

    def decrease_active_rentals(self, n_tools):
        self.active_rentals -= n_tools

    def get_random_nights(self):
        return randint(self.min_nights, self.max_nights)

    def get_random_tool_category_map(self, categories):
        tool_category_map = {}

        for selection in range(randint(1,2)):
            num_tools = randint(self.min_tools, self.max_tools)
            for i in range(0, num_tools):
                category = categories[randint(0, 4)]
                tool_category_map[category] = 1

        return tool_category_map

class BusinessCustomer(Customer):
    def __init__(self, name):
        super().__init__(name, 7, 7, 3, 3)


class RegularCustomer(Customer):
    def __init__(self, name):
        super().__init__(name, 3, 5, 1, 3)


class CasualCustomer(Customer):
    def __init__(self, name):
        super().__init__(name, 1, 2, 1, 2)


