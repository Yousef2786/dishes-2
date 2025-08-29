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

    
#calling the add_dish() function.
food = Dish()

food.add_dish("Steak", "Beef and salt", ["Savory", "Beefy"])


# Printing the dishes_list to see the result.
print(food.dishes_list)

# This works as intended so far.
#----------------------------------------------------------

# Finding a dish based on the flavor chosen with find_dish():

flavor_chosen = food.find_dish("Savory")
print(flavor_chosen)
