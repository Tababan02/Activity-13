plant_types_dict = {
    "Oak" : "Tree",
    "Rose" : "Shrub",
    "Basil" : "Herb",
    "Maple" : "Tree",
    "Lavender" : "Herb",
    "Holly" : "Shrub",
    "Sunflower" : "Annual",
    "Cactus" : "Succulent"
} 
# 2
print(plant_types_dict)

# 3
print("The type of the 5th plant is ", "Lavender")
      
# 4
plant_types_dict["Rose"] = "Annual"

# 5
del plant_types_dict["Holly"]
 
# 2 
print(plant_types_dict)

# 6
last_key = list(plant_types_dict.keys())[-1]
last_value = plant_types_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)