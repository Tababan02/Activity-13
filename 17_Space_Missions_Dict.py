space_missions_dict = {
  "Apollo 11": "1969",
  "Voyager 1": "1977",
  "Space Shuttle Columbia": "1981",
  "Mars Rover Spirit": "2004",
  "International Space Station (ISS)": "1998"
}

# 2
print(space_missions_dict)

# 3
print(space_missions_dict['Mars Rover Spirit'])

# 4
space_missions_dict["Space Shuttle Columbia"] = "2024"

# 5
del space_missions_dict['International Space Station (ISS)']

# 2
print(space_missions_dict)

# 6
last_key = list(space_missions_dict.keys())[-1]
last_value = space_missions_dict[last_key]
print("The last key-value pair is ", last_value, ":",last_key)