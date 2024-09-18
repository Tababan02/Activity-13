element_symbols_dict = {
    "Hydrogen": "H",
    "Helium": "He",
    "Lithium": "Li",
    "Beryllium": "Be",
    "Boron": "B",
    "Carbon": "C",
    "Nitrogen": "N",
    "Oxygen": "O",
    "Fluorine": "F",
    "Neon": "Ne",
}

# 1
print(element_symbols_dict)

# 2
print("The symbol of the 6th element is ",element_symbols_dict["Nitrogen"])

# 3
element_symbols_dict["Fluorine"] = 'A'

# 4
del element_symbols_dict["Neon"]

# 2 
print(element_symbols_dict)

# 6
last_key = list(element_symbols_dict.keys())[-1]
last_value = element_symbols_dict[last_key]
print("The last key-value pair is ", last_key, ":" , last_value)
 