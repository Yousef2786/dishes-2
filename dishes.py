# A list for adding dictionaries of dishes that includ the dish_name, dish_recipe, and dish_flavor.
dishes_list = []



class Dish:
    def __init__(self):
        pass

# A method to append dishes to the dishes_list as dictionary.        
    def add_dish(self, dish_name, dish_recipe, dish_flavor):
        dict_dishes = {"Dish": dish_name, "Recipe": dish_recipe, "Flavor Profile": dish_flavor}
        dishes_list.append(dict_dishes)

    def find_dish(self, flavor):
        for fl in dishes_list:
            if flavor in fl.values():
                print(f"Here's the dish we recommend to you: {fl}")

    
#calling the add_dish() function.
food = Dish()
food.add_dish("Steak", "Beef and salf", "Savory")


# Printing the dishes_list to see the result.
print(dishes_list)

# This works as intended so far.
#----------------------------------------------------------

# Finding a dish based on the flavor chosen with find_dish():

food.find_dish("Savory")