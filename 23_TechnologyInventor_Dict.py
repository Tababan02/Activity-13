technology_inventors_dict = {
    "Telephone" : "Alexander Graham Bell",
    "Light Bulb" : "Thomas Edison",
    "Internet" : "Tim Berners-Lee",
    "Radio" : "Guglielmo Marconi",
    "Airplane" : "Wright Brothers",
    "Computer" : "Charles Babbage"
}
# 2
print(technology_inventors_dict)

# 3
print("the inventor of the 4th genre is ",["Radio"])
      
# 4
technology_inventors_dict["Light Bulb"] = ['Sandara']

# 5
del technology_inventors_dict["Computer"]
 
# 2 
print(technology_inventors_dict)

# 6
last_key = list(technology_inventors_dict.keys())[-1]
last_value = technology_inventors_dict[last_key]
print("The last key-value pair is ", last_value, ":",last_key)