coffee_types_dict = {
  "Espresso" : "Strong, concentrated coffee brewed under pressure.",
  "Americano" : "Espresso diluted with hot water.",
  "Cappuccino" : "Espresso with steamed milk and milk foam.", 
  "Latte" : "Espresso with steamed milk, topped with foam.",
  "Mocha" : "Latte with chocolate syrup and whipped cream.",
  "Macchiato" : "Espresso 'stained' with a bit of milk.",
  "Flat White" : "Strong coffee with velvety microfoam.",
  "Cold Brew" : "Coffee brewed cold for a smooth flavor.",
  "Affogato" : "Espresso poured over vanilla ice cream.",
  "Turkish Coffee" : "Finely ground coffee brewed unfiltered."
}

# 2
print(coffee_types_dict)

# 3
print("The description of the 4th type of coffee is ", "Latte")
      
# 4
coffee_types_dict["Cold Brew"] = "Brewed with cold rather than hot water"

# 5
del coffee_types_dict["Mocha"]
 
# 2 
print(coffee_types_dict)

# 6
last_key = list(coffee_types_dict.keys())[-1]
last_value = coffee_types_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)