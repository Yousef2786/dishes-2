# A list for adding dictionaries of dishes that includ the dish_name, dish_recipe, and dish_flavor.

class Dish:
    def __init__(self):
        self.dishes_list = []

# A method to append dishes to the dishes_list as dictionary.        
    def add_dish(self, dish_name, dish_recipe, dish_flavor):
        dict_dishes = {"Dish": dish_name, "Recipe": dish_recipe, "Flavor Profile": dish_flavor}
        self.dishes_list.append(dict_dishes)

    def find_dish(self, flavor):
        recommended_dish = [dish for dish in self.dishes_list if flavor in dish["Flavor Profile"]]
        if recommended_dish:
            return f"We recommend the following dish: {recommended_dish}"
        else:
            return "We don't have a dish with that flavor profile."

    
# calling the add_dish() function.
food = Dish()

food.add_dish("Steak", "Beef and salt", ["Savory", "Beefy"])
food.add_dish("Mashed Potatoes", "Potatoes and butter", ["Savory", "Buttery"])

# Function for interactive mode using input():

def interactive_mode():
    while True:
        print("\n...This is where we add a dish...\n")
        name = input("Name your dish (press 'q' to stop): ")
        if name == 'q':
            break
        recipe = input("Add your recipe: ")
        flavors_input = input("Add the flavor profile(s) of this dish separated by a comma: ")
        flavors_list = [flavors_input.strip() for flavor in flavors_input.split(",")]

        food.add_dish(name, recipe, flavors_list)
        print("\nCurrent dishes in database: ")
        print(food.dishes_list)



# Printing the dishes_list to see the result.
print(f" - List of dishes: {food.dishes_list}")

# This works as intended so far.
#----------------------------------------------------------

# Finding a dish based on the flavor chosen with find_dish():

flavor_chosen = food.find_dish("Buttery")
print(f" - {flavor_chosen}")
