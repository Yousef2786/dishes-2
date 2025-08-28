# A list for adding dictionaries of dishes that includ the dish_name, dish_recipe, and dish_flavor.
dishes_list = []

# A function to append dishes to the dishes_list as dictionary.
def add_dish(dish_name, dish_recipe, dish_flavor):
    dict_dishes = {"Dish": dish_name, "Recipe": dish_recipe, "Flavor Profile": dish_flavor}
    dishes_list.append(dict_dishes)
    

# Gathering inputs for the add_dish(dish_name, dish_recipe, dish_flavor) function.
dish_name = input("What's the name of your dish? ")
dish_recipe = input("Add your dish recipe here: ")
dish_flavor = input("What are the flavor profiles for this dish? ")

#calling the add_dish() function.
add_dish(dish_name, dish_recipe, dish_flavor)

# Printing the dishes_list to see the result.
print(dishes_list)

# This works as intended so far.
#----------------------------------------------------------

