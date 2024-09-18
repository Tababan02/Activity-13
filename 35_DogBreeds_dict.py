dog_breeds_dict = {
    "Chihuahua" : "Small",
    "Beagle" : "Medium",
    "Golden Retriever" : "Large",
    "Poodle" : "Medium",
    "Dachshund" : "Small",
    "Bulldog" : "Medium",
    "Siberian Husky" : "Large",
    "Shih Tzu" : "Small",
    "Boxer" : "Large",
    "Cocker Spaniel" : "Medium",
}
  
# 2
print(dog_breeds_dict)

# 3
print("The size of the 5th breed is ", "Dachshund")
      
# 4
dog_breeds_dict["Shih Tzu"] = "Medium"

# 5
del dog_breeds_dict["Bulldog"]
 
# 2 
print(dog_breeds_dict)

# 6
last_key = list(dog_breeds_dict.keys())[-1]
last_value = dog_breeds_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)