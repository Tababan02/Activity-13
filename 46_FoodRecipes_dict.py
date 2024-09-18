food_recipes_dict = {
  "Spaghetti Carbonara" : "Cook spaghetti; mix with pancetta, eggs, and cheese.",
  "Chicken Curry" : "Sauté onions; add chicken and coconut milk; simmer.",
  "Guacamole" : "Mash avocados; mix with lime, onion, tomato, and cilantro.",
  "Chocolate Chip Cookies" : "Mix butter, sugar, eggs, flour, and chocolate chips; bake.",
  "Caprese Salad" : "Layer mozzarella, tomatoes, and basil; drizzle with olive oil.",
  "Beef Tacos" : "Cook ground beef; serve in tortillas with toppings.",
  "Vegetable Stir-fry" : "Sauté vegetables in oil; add soy sauce.",
  "Pumpkin Soup" : "Cook pumpkin and onion; blend with broth and season.",
}

# 2
print(food_recipes_dict)

# 3
print("the recipe of the 5th food is ", "Caprese Salad")
      
# 4
food_recipes_dict["Guacamole"] = "Avocado, Lemon"

# 5
del food_recipes_dict["Vegetable Stir-fry"]
 
# 2 
print(food_recipes_dict)

# 6
last_key = list(food_recipes_dict.keys())[-1]
last_value = food_recipes_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)