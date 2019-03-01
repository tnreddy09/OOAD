# Running the simulation

>python3 simulation.py

To run the rental store simulation we have to run the "simulation.py" file in the repository.

# Classes description

## Customer:
Customer Base class has different attributes like the name of the customer, minimum and maximum number of tools he can rent, minimum and maximum number of nights he can rent and also his active rentals.
Each type of customer derives from the Base Customer class and implements the is_valid_request method to check whether according to the customer type whether it is a valid rental request or not.

## Rental Store Class:
Rental Store has an inventory in which different categories (sections) of tools are maintained.
Rental Store is also responsible for maintaining the inventory which includes checking for the availability of a tool when a rental request arrives, renting the tools and also updating the tools availability when the tools are returned,  maintaining a list of “active rentals”, “completed rentals”, “customer list” and total amount of revenue.

## Inventory Class:
Inventory class has different sections(Categories) of tools in it. It has APIs to get the tool information and update the tool information while rental is done.

## Rental Class
In the Rental class, we have attributes to store all the information related to a particular rental like the customer involved in the rental, rental day, day of return, tools rented in the rental, total amount of the rental.

## Section Class:
Section class has various attributes like the name of the category,  price of the tools in the category, Number of tools in the category

## Simulation Description:

We run the simulation in a while loop, where in each iteration we will be doing the following tasks.
1. Increment the day
2. Check the active rentals list to check if any rentals has to be closed.
3. Report all the rentals closed at the day
4. Select a random customer from the customer list
5. Select the random number of tools and days according to the customer class selected
6. Create a customer request
7. Process request by calling the rent method in the Rental store.
8. Print all the rentals for the day.

If simulation has to run we have execute the “simulation.py” file.

## Output of the Simulation
[link to simulation output!](https://github.com/AkritiKapur/OOAD/blob/master/Assignment03/simulation_output.txt)
