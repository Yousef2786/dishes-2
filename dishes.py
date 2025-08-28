# A list for adding dictionaries of dishes that includ the dish_name, dish_recipe, and dish_flavor.

class Dish:
    def __init__(self):
        self.dishes_list = []

# A method to append dishes to the dishes_list as dictionary.        
    def add_dish(self, dish_name, dish_recipe, dish_flavor):
        dict_dishes = {"Dish": dish_name, "Recipe": dish_recipe, "Flavor Profile": dish_flavor}
        self.dishes_list.append(dict_dishes)

    def find_dish(self, flavor):
        result = [fl for fl in self.dishes_list if flavor in fl.values()]
        return result

    
#calling the add_dish() function.
food = Dish()

dish_name = input("Name your dish: ")
dish_recipe = input("Add your recipe: ")
dish_flavor = input("What is this dish's flavor profile? ")

food.add_dish(dish_name, dish_recipe, dish_flavor)


# Printing the dishes_list to see the result.
print(food.dishes_list)

# This works as intended so far.
#----------------------------------------------------------

# Finding a dish based on the flavor chosen with find_dish():

flavor_profile = input("What flavor profile are you looking for? ")

recommend_dish = food.find_dish(flavor_profile)

print(f"We recommend the following dish: {recommend_dish}")