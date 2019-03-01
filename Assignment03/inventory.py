"""
    Inventory of the store
"""


class Inventory:
    def __init__(self):
        pass


class Section:
    def __init__(self, name, price, n_tools):
        self.category_name = name
        self.price = price
        self.tools = self.add_tools(n_tools)

    def add_tools(self, tool_count):
        tools = []
        for i in range(tool_count):
            tools.append("{} - {}".format(self.category_name, i))

        return tools
