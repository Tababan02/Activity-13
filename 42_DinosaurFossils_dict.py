dinosaur_fossils_dict = {
    "Tyrannosaurus Rex" : "North America",
    "Triceratops" : "North America",
    "Brachiosaurus" : "North America, Africa",
    "Velociraptor" : "Mongolia",
    "Stegosaurus" : "North America",
    "Spinosaurus" : "North Africa",
    "Ankylosaurus" : "North America",
} 

# 2
print(dinosaur_fossils_dict)

# 3
print("The location of the 4th dinousaur's fossils ", "Velociraptor")
      
# 4
dinosaur_fossils_dict["Triceratops"] = "Philippines"

# 5
del dinosaur_fossils_dict["Spinosaurus"]
 
# 2 
print(dinosaur_fossils_dict)

# 6
last_key = list(dinosaur_fossils_dict.keys())[-1]
last_value = dinosaur_fossils_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)