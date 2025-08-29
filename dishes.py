# A list for adding dictionaries of dishes that includ the dish_name, dish_recipe, and dish_flavor.

class Dish:
    def __init__(self):
        self.dishes_list = []

# A method to append dishes to the dishes_list as dictionary.        
    def add_dish(self, dish_name, dish_recipe, dish_flavor):
        dict_dishes = {"Dish": dish_name, "Recipe": dish_recipe, "Flavor Profile": dish_flavor}
        self.dishes_list.append(dict_dishes)

    def find_dish(self, flavor):
        result = None
        for dish_dict in self.dishes_list:
            if flavor in dish_dict["Flavor Profile"]:
                recommended_dish = []
                recommended_dish.append(dish_dict)
                result = f"We recommend the following dish: {recommended_dish}"
            else:
                result = "We don't have a dish with that flavor profile."
        return result

    
#calling the add_dish() function.
food = Dish()

food.add_dish("Steak", "Beef and salt", ["Savory", "Beefy"])


# Printing the dishes_list to see the result.
print(food.dishes_list)

# This works as intended so far.
#----------------------------------------------------------

# Finding a dish based on the flavor chosen with find_dish():

flavor_chosen = food.find_dish("Umami")
print(flavor_chosen)
