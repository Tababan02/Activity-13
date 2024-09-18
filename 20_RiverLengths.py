river_lengths_dict = {
    "Nile" : "6,650 km",
  "Amazon" : "6,400 km",
  "Yangtze" : "6,300 km",
  "Mississippi-Missouri" : "6,275 km",
  "Yenisei" : "5,539 km",
  "Yellow River (Huang He)" : "5,464 km",
  "Ob-Irtysh" : "5,410 km",
  "Río de la Plata" : "4,880 km",
  "Congo" : "4,700 km",
  "Amur-Argun" : "4,444 km",
}

# 2 
print(river_lengths_dict)

# 3
print("the length of the 2nd river is ", ['Yangtze'])

# 4 
river_lengths_dict["Yellow River (Huang He)"] = "6,000km"

# 5
del river_lengths_dict['Yenisei']

# 2
print(river_lengths_dict)

# 6
last_key = list(river_lengths_dict.keys())[-1]
last_value = river_lengths_dict[last_key]
print("The last key-value pair is ", last_key, ":", last_value)