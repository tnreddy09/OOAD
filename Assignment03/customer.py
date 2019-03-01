"""
    Customer Information
"""


class Customer:
    def __init__(self, name, min_nights, max_nights, min_tools, max_tools):
        self.name = name
        self.min_nights = min_nights
        self.max_nights = max_nights
        self.min_tools = min_tools
        self.max_tools = max_tools

    def is_valid_request(self, n_tools, n_nights):
        if (self.min_nights <= n_nights <= self.max_nights) and \
                (self.min_tools <= n_tools <= self.max_tools):
            return True
        return False


class BusinessCustomer(Customer):
    def __init__(self, name):
        super().__init__(name, 7, 7, 3, 3)


class RegularCustomer(Customer):
    def __init__(self, name):
        super().__init__(name, 3, 5, 1, 3)


class CasualCustomer(Customer):
    def __init__(self, name):
        super().__init__(name, 1, 2, 1, 2)

