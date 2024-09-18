historical_events_dict ={
  "American Declaration of Independence" : 1776,
  "French Revolution" : 1789,
  "World War I Begins" : 1914,
  "World War II Begins" : 1939,
  "Moon Landing" : 1969,
  "Fall of the Berlin Wall" : 1989,
  "September 11 Attacks" : 2001,
  "COVID-19 Pandemic Declared" : 2020,
}   
  
# 2
print(historical_events_dict)

# 3
print("The year of the 2nd event is ", "French Revolution")
      
# 4
historical_events_dict["September 11 attacks"] = "2002"

# 5
del historical_events_dict["Moon Landing"]
 
# 2 
print(historical_events_dict)

# 6
last_key = list(historical_events_dict.keys())[-1]
last_value = historical_events_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)