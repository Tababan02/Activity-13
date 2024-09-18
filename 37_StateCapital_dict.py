state_capitals_dict = {
  "Alabama" : "Montgomery",
  "Alaska" : "Juneau",
  "Arizona" : "Phoenix",
  "Arkansas" : "Little Rock",
  "California" : "Sacramento",
  "Colorado" : "Denver",
  "Connecticut" : "Hartford",
  "Delaware" : "Dover",
  "Florida" : "Tallahassee",
  "Georgia" : "Atlanta",
} 
# 2
print(state_capitals_dict)

# 3
print("The capital of the 4th state is ", "Arkansas")
      
# 4
state_capitals_dict["Florida"] = "Manila"

# 5
del state_capitals_dict["Connecticut"]
 
# 2 
print(state_capitals_dict)

# 6
last_key = list(state_capitals_dict.keys())[-1]
last_value = state_capitals_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)