from Assignment03.inventory import Inventory, Section
from Assignment03.customer import  Customer, BusinessCustomer, RegularCustomer, CasualCustomer
from Assignment03.store import Store
from random import randint

customer_list = ["Customer 1", "Customer 2", "Customer 3",
                 "Customer 4", "Customer 5", "Customer 6",
                 "Customer 7", "Customer 8", "Customer 9",
                 "Customer 10"]

customer_types = ["Business", "Regular", "Casual"]

tool_types = ["Painting", "Concrete", "Plumbing", "Woodwork", "Yardwork"]
tool_prices = [50, 10, 8, 15, 16]
tool_nums = [2, 6, 3, 4, 5]

TOTAL_NUM_DAYS=5

if __name__ == "__main__":
    day_num = 0
    customers = []

    #create a list of customers
    for customer in customer_list:
        r = randint(0, 2)
        cust = None
        if r == "Business":
            cust = BusinessCustomer(customer)
        elif r == "Regular":
            cust = RegularCustomer(customer)
        else:
            cust = CasualCustomer(customer)
        customers.append(cust)

    #creating an inventory
    sections = []
    for name, price, n_tools in zip(tool_types, tool_prices,
                                    tool_nums):
        section = Section(name, price, n_tools)
        sections.append(section)

    inventory = Inventory(sections)

    #creating a rental store object
    rentalStore = Store(inventory, customers)



    while day_num < TOTAL_NUM_DAYS:
        print("DAY NUMBER - {}".format(day_num))
        print("\n\n")
        day_num += 1

        print("RETURNED RENTALS")
        rentalStore.update_rentals(day_num)

        print("*" * 100)

        #select a random customer
        r = randint(0, 9)
        random_customer = customers[r]
        tool_category_map = random_customer.get_random_tool_category_map(tool_types)
        num_nights = random_customer.get_random_nights()

        print("RENTALS")
        rentalStore.rent_tool(random_customer, num_nights, tool_category_map, day_num)

        print("*" * 100)

    print("\n\n")
    print("END OF SIMULATION")
    print("Total Revenue of the Store ${}".format(rentalStore.amount))

    sections = inventory.get_sections()
    tools_remaining = []
    for name in sections:
        for tool in sections[name].get_tools():
            tools_remaining.append("Tool: {}, Category: {}".format(tool, name))


    print("Tools Remaining - {}".format(len(tools_remaining)))

    for tool in tools_remaining:
        print(tool)

    print("\n\n")
    print("*" * 100)
    print("Active Rentals")
    print("*" * 100)

    active_rentals = rentalStore.get_active_rentals()

    print("Total - {}".format(len(active_rentals)))

    for active_rental in active_rentals:
        active_rental.print_report("RENTED")

    print("*" * 100)

    print("Completed Rentals")

    print("*" * 100)

    completed_rentals = rentalStore.get_completed_rentals()
    print("Total - {}".format(len(completed_rentals)))

    for completed_rental in completed_rentals:
        completed_rental.print_report("RETURNED")

    print("*" * 100)





