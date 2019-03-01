from Assignment03.inventory import Inventory, Section
from Assignment03.customer import  Customer, BusinessCustomer, RegularCustomer, CasualCustomer
from Assignment03.store import Store
from random import randint

#list of different customer names that will be created
customer_list = ["Customer 1", "Customer 2", "Customer 3",
                 "Customer 4", "Customer 5", "Customer 6",
                 "Customer 7", "Customer 8", "Customer 9",
                 "Customer 10"]

#3 different types of customer
customer_types = ["Business", "Regular", "Casual"]

#5 different types of tool categories
tool_types = ["Painting", "Concrete", "Plumbing", "Woodwork", "Yardwork"]
#prices of each of the tool category
tool_prices = [50, 10, 8, 15, 16]
#number of tools under each category
tool_nums = [2, 6, 3, 4, 5]

#the total number of days that the simulation needs to run
TOTAL_NUM_DAYS=35


'''
    The below code is the main function where the simulator code is executed.
    Initially the following things are done before the simulation begins:
        1. Creating 10 customer objects
        2. Creating an inventory
        3. Creating a rental store object
    
    The following steps are executed in order in the simulator logic:
        1. Incrementing the day
        2. Updating the rental store searching for returned rentals
        3. Randomly choosing a set of customers
        4. For each of the randomly chosen customers, a random set of categories \
            and number of tools chosen under each category is decided.
        5. From the above created categories and the number of tools per category, \
            we rent those tools by calling the rent_tool function of the store class.
    
    Finally, after the simulator runs, the following information is printed out:
        1. The total revenue of the rental store
        2. The tools remaining in each of the different tool sections/categories
        3. Active rentals present
        4. Completed rentals
            
            
'''

if __name__ == "__main__":
    day_num = 0
    customers = []
    # counter = 0

    #create a list of customers
    for customer in customer_list:
        r = randint(0, 2)
        cust = None
        if customer_types[r] == "Business":
            # print("COUNTER BUSINESS %d"%counter)
            cust = BusinessCustomer(customer)
        elif customer_types[r] == "Regular":
            # print("COUNTER REGULAR %d"%counter)
            cust = RegularCustomer(customer)
        else:
            # print("COUNTER CASUAL %d"%counter)
            cust = CasualCustomer(customer)
        # counter += 1
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

    print("*" * 100)
    print("CUSTOMERS OF THE STORE")
    print("*" * 100)

    for cust in customers:
        cust.print_customer_info()
        # print(cust.name)

    print("\n\n")

    #simulation begins
    while day_num < TOTAL_NUM_DAYS:
        print("*" * 100)

        print("DAY NUMBER - {}".format(day_num))
        print("*" * 100)

        print("\n")
        day_num += 1
        print("*" * 100)
        print("RETURNED RENTALS")
        print("*" * 100)

        rentalStore.update_rentals(day_num)

        print("*" * 100)
        print("RENTALS")
        print("*" * 100)

        #select a random customer
        for c in range(1, 4):
            r = 0
            if c == 1:
                r = randint(0, 3)
            elif c == 2:
                r = randint(4, 7)
            else:
                r = randint(8, 9)

            random_customer = customers[r]
            tool_category_map = random_customer.get_random_tool_category_map(tool_types)
            num_nights = random_customer.get_random_nights()

            #rent tools from the above chosen tool categories
            #print("RENTALS")
            rentalStore.rent_tool(random_customer, num_nights, tool_category_map, day_num)

        print("*" * 100)

    #Calculating TOTAL REVENUE of the store after the simulation ends
    print("\n")

    print("*" * 100)
    print("END OF SIMULATION")
    print("*" * 100)

    print("\n")
    print("Total Revenue of the Store ${}".format(rentalStore.amount))
    print("\n")

    #Calculating Tools remaining in each of the tool sections/categories \
    # after the simulation ends
    sections = inventory.get_sections()
    tools_remaining = []
    for name in sections:
        for tool in sections[name].get_tools():
            tools_remaining.append("Tool: {}, Category: {}".format(tool, name))

    print("\n")
    print("Tools Remaining - {}".format(len(tools_remaining)))
    print("\n")

    for tool in tools_remaining:
        print(tool)

    #Printing out the Active Rentals that are still present after \
    # the simulation ends
    print("\n")
    print("*" * 100)
    print("Active Rentals")
    print("*" * 100)

    active_rentals = rentalStore.get_active_rentals()

    print("Total - {}".format(len(active_rentals)))

    for active_rental in active_rentals:
        active_rental.print_report("RENTED")

    print("*" * 100)

    # Printing out the Completed Rentals after the simulation ends
    print("Completed Rentals")

    print("*" * 100)

    completed_rentals = rentalStore.get_completed_rentals()
    print("Total - {}".format(len(completed_rentals)))

    for completed_rental in completed_rentals:
        completed_rental.print_report("RETURNED")

    print("*" * 100)





