# A list for adding dictionaries of dishes that includ the dish_name, dish_recipe, and dish_flavor.
dishes_list = []



class Dish:
    def __init__(self):
        pass

# A method to append dishes to the dishes_list as dictionary.        
    def add_dish(self, dish_name, dish_recipe, dish_flavor):
        dict_dishes = {"Dish": dish_name, "Recipe": dish_recipe, "Flavor Profile": dish_flavor}
        dishes_list.append(dict_dishes)

    
#calling the add_dish() function.
steak = Dish()
steak.add_dish("Steak", "Beef and salf", "Savory")


# Printing the dishes_list to see the result.
print(dishes_list)

# This works as intended so far.
#----------------------------------------------------------

