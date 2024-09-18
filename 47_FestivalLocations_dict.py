festival_locations_dict = {
  "Oktoberfest" : "Munich, Germany",
  "Carnival" : "Rio de Janeiro, Brazil",
  "Holi" : "India",
  "Diwali" : "India",
  "Coachella" : "California, USA",
  "Running of the Bulls" : "Pamplona, Spain",
  "Harbin Ice Festival" : "Harbin, China",
  "Tomorrowland" : "Boom, Belgium",
  "Burning Man" : "Black Rock City, Nevada, USA",
  "Chinese New Year" : "China and worldwide",

}

# 2
print(festival_locations_dict)

# 3
print("the  location of the 4th festival is ", "Diwali")
      
# 4
festival_locations_dict["Running of the Bulls"] = "Philippines"

# 5
del festival_locations_dict["Carnival"]
 
# 2 
print(festival_locations_dict)

# 6
last_key = list(food_recipes_dict.keys())[-1]
last_value = food_recipes_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)