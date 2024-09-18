sports_events_dict = {
  "Summer Olympics" : "2021",
  "FIFA World Cup" : "2018",
  "Super Bowl" : "2023",
  "Wimbledon" : "2022",
  "NBA Finals" :"2022",
  "Tour de France" : "2022",
  "UEFA Champions League Final" : "2022"
}

# 2
print(sports_events_dict)

# 3
print("the year of the 3rd sports event is ", "Super Bowl")
      
# 4
sports_events_dict["Tour de France"] = "2024"

# 5
del sports_events_dict ["NBA Finals"]
# 2 
print(sports_events_dict)

# 6
last_key = list(sports_events_dict.keys())[-1]
last_value = sports_events_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)