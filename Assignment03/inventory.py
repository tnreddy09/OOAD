"""
    Inventory of the store

    This class holds the information about the
    different tool sections/categories.

    Initially, an inventory is created by creating an object
    of this class, creating sections and populating tools into each
    of this section.

    Main Responsibilities include:
        1. Adding new sections and tools to the inventory.
        2. A check for the number of tools before a transaction is processed
        3. Handling the renting of the tools
        4. Handling the returning of the tools

    The handling of the renting and the returning of the tools is delegated from
    the inventory class to the Section class.
"""


class Inventory:
    def __init__(self, categories):
        self.sections = self.allocate_tools(categories)

    def allocate_tools(self, sections):
        section_dict = {}
        for section in sections:
            section_dict[section.category_name] = section
        return section_dict

    def get_sections(self):
        return self.sections

    def add_section(self, section):
        self.sections[section.name] = section

    def is_valid_request(self, tool_category_map):
        is_valid = True
        for category_name,n_tools in tool_category_map.items():
            is_valid = is_valid and (category_name in self.sections) and len(self.sections[category_name].tools) >= n_tools
        return is_valid

    def rent_tools(self, tool_category_map):
        rented_tools = {}
        for category_name, n_tools in tool_category_map.items():
            rented_tools[category_name] = self.get_section(category_name).rent_tools(n_tools)
        return rented_tools

    def get_section(self, section_name):
        return self.sections[section_name]

    def return_tools(self, tool_category_map):
        for category_name, tools in tool_category_map.items():
            section = self.get_section(category_name)
            section.return_tools(tools)


"""
    Section class
    
    This class holds the information of a particular category
    
    The categories as mentioned in the problem statement can be follows:
        1. Painting 
        2. Concrete
        3. Plumbing
        4. Woodwork
        5. Yardwork
    
    This class holds the following information:
        1. Name of the category
        2. Price of the tools in the category
        3. Number of tools in the category
        
    Main responsibilities of this class includes:
        1. Adding tools to the section - called during init time by the Inventory object
        2. Rent tools from this section
        3. Returning tools to this section
        4. Returning the price of the tools in this section.
    
    
"""

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

    def rent_tools(self, n_tools):
        rented_tools = self.tools[len(self.tools) - n_tools: len(self.tools)][::-1]
        self.tools = self.tools[:len(self.tools) - n_tools]
        return rented_tools

    def get_tools(self):
        return self.tools

    def return_tools(self, tools):
        self.tools = self.tools + tools

    def get_price(self):
        return self.price


# if __name__ == '__main__':
#     # add section
#     sections = []
#     for name, price, n_tools in zip(["Painting", "Concrete", "Plumbing", "Woodwork", "Yardwork"], [50, 10, 8, 15, 16], [2, 6, 3, 4, 5]):
#         section = Section(name, price, n_tools)
#         sections.append(section)
#
#     inventory = Inventory(sections)
#
#     for section in inventory.sections:
#         print(section, inventory.sections[section].price)
