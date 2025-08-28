dishes_list = []

def add_dish(dish_name, dish_recipe, dish_flavor):
    dict_dishes = {"Dish": dish_name, "Recipe": dish_recipe, "Flavor Profile": dish_flavor}
    dishes_list.append(dict_dishes)
    

# Gather inputs first
dish_name = input("What's the name of your dish? ")
dish_recipe = input("Add your dish recipe here: ")
dish_flavor = input("What are the flavor profiles for this dish? ")

add_dish(dish_name, dish_recipe, dish_flavor)

print(dishes_list)