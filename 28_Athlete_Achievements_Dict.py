athlete_achievements_dict = {
    "Michael Phelps" : "23 Olympic gold medals in swimming",
    "Usain Bolt" : "World record holder in 100m and 200m sprints",
    "Serena Williams" : "23 Grand Slam singles titles in tennis",
    "Tom Brady" : "7 Super Bowl championships in American football",
    "Michael Jordan" : "6 NBA championships and 5 MVP awards",
    "Roger Federer" : "20 Grand Slam singles titles in tennis",
    "Simone Biles" : "7 Olympic medals, including 4 golds in gymnastics",
    "Lionel Messi" : "7 Ballon d'Or awards in football (soccer)"
}

# 2
print(athlete_achievements_dict)

# 3
print("The achievement of the 5th athlete is ",["Michael Jordan"])
      
# 4
athlete_achievements_dict["Serena Willian"] = ["champion in grand slam 2024"]

# 5
del athlete_achievements_dict["Simone Biles"]
 
# 2 
print(athlete_achievements_dict)

# 6
last_key = list(athlete_achievements_dict.keys())[-1]
last_value = athlete_achievements_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)