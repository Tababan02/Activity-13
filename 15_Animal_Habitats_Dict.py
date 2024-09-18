animal_habitats_dict = {
  "Lion": "Savanna",
  "Penguin": "Antarctic Ice",
  "Elephant": "Grasslands",
  "Polar Bear": "Arctic Tundra",
  "Dolphin": "Oceans",
  "Kangaroo": "Australian Bush",
  "Giraffe": "Savanna",
  "Tiger": "Tropical Rainforest",   
}

# 2 
print(animal_habitats_dict)

# 3 
print("The habitat of the 3rd animal ", animal_habitats_dict["Polar Bear"])

# 4
animal_habitats_dict["Kangaroo"] = 'Mountains'

# 5
del animal_habitats_dict["Tiger"]

# 2
print(animal_habitats_dict)

# 6
last_key = list(animal_habitats_dict.keys())[-1]
last_value = animal_habitats_dict[last_key]
print("The last key-value pair is " ,last_value, ":", last_key)
