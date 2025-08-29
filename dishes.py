# Classes:

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

class User:
    def __init__(self, name, preferred_flavors):
        self.name = name
        self.preferred_flavors = preferred_flavors
    
    def get_recommendation(self):
        recommended_dish = []
        for fl_i in self.preferred_flavors:
            for dishes_i in food.dishes_list:
                if fl_i in dishes_i["Flavor Profile"] and dishes_i not in recommended_dish:
                    recommended_dish.append(dishes_i)
        return f"Based on {self.name}'s preferred flavor profiles, here are his recommended dishes: {recommended_dish}"

#-Classes end--------------------------------------------------------------------

# calling the add_dish() function.
food = Dish()

food.add_dish("Steak", "Beef and salt", ["Savory", "Beefy"])
food.add_dish("Mashed Potatoes", "Potatoes and butter", ["Savory", "Buttery"])
food.add_dish("Misou soup", "Dashi and hot water", ["Umami"])

#----Function for interactive mode using input():------------------------

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

#--Interactive mode end---------------------------------------------------------------------------

# Printing the dishes_list to see the result.
print(f" - List of dishes: {food.dishes_list}")

# This works as intended so far.
#----------------------------------------------------------

# Finding a dish based on the flavor chosen with find_dish():

flavor_chosen = food.find_dish("Buttery")
print(f" - {flavor_chosen}")

john = User("John", ["Savory", "Buttery"])
recommendation_john = john.get_recommendation()
print(recommendation_john)