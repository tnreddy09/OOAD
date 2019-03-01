"""
    Inventory of the store
"""


class Inventory:
    def __init__(self, categories):
        self.n_items = 20
        self.sections = self.allocate_tools(categories)

    def allocate_tools(self, sections):
        section_dict = {}
        for section in sections:
            section_dict[section.category_name] = section
        return section_dict

    def add_section(self, section):
        self.sections[section.name] = section


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


if __name__ == '__main__':
    # add section
    sections = []
    for name, price, n_tools in zip(["Painting", "Concrete", "Plumbing", "Woodwork", "Yardwork"], [50, 10, 8, 15, 16], [2, 6, 3, 4, 5]):
        section = Section(name, price, n_tools)
        sections.append(section)

    inventory = Inventory(sections)

    for section in inventory.sections:
        print(section, inventory.sections[section].price)
