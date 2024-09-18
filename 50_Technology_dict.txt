technology_innovators_dict = {
  "Personal Computer" : "Steve Jobs, Bill Gates",
  "Internet" : "Tim Berners-Lee",
  "Electric Light Bulb" : "Thomas Edison",
  "Telephone" : "Alexander Graham Bell",
  "Automobile" : "Henry Ford",
  "Airplane" : "Wright Brothers",
  "Smartphone" : "Steve Jobs",
  "GPS" : "Roger L. Easton"
}

# 2
print(technology_innovators_dict)

# 3
print("the  innovator of the 4th technology is ", "Telephone")
      
# 4
technology_innovators_dict["Internet"] = "Sandara"

# 5
del technology_innovators_dict ["Airplane"]

# 2 
print(technology_innovators_dict)

# 6
last_key = list(technology_innovators_dict.keys())[-1]
last_value = technology_innovators_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)