"""
    Inventory of the store
"""


class Inventory:
    def __init__(self, categories):
        self.sections = self.allocate_tools(categories)

    def allocate_tools(self, sections):
        section_dict = {}
        for section in sections:
            section_dict[section.category_name] = section
        return section_dict

    def add_section(self, section):
        self.sections[section.name] = section

    def is_valid_request(self, category_name, n_tools):
        return (category_name in self.sections) and len(self.sections[category_name].tools) <= n_tools

    def rent_tools(self, category_name, n_tools):
        rented_tools = self.sections[category_name].rent_tools(n_tools)
        return rented_tools

    def get_section(self, section_name):
        return self.sections[section_name]


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
        return self.tools[len(self.tools) - n_tools: len(self.tools)][::-1]


if __name__ == '__main__':
    # add section
    sections = []
    for name, price, n_tools in zip(["Painting", "Concrete", "Plumbing", "Woodwork", "Yardwork"], [50, 10, 8, 15, 16], [2, 6, 3, 4, 5]):
        section = Section(name, price, n_tools)
        sections.append(section)

    inventory = Inventory(sections)

    for section in inventory.sections:
        print(section, inventory.sections[section].price)
