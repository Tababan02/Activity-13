video_game_platforms_dict = {
    "The Legend of Zelda: Breath of the Wild" : "Nintendo Switch",
    "God of War" : "PlayStation 4",
    "Minecraft" : "Multi-platform",
    "Call of Duty: Warzone" : "PC, PlayStation, Xbox",
    "Super Mario Odyssey" : "Nintendo Switch",
    "Red Dead Redemption 2" : "PC, PlayStation, Xbox",
    "Fortnite" : "Multi-platform",
    "The Witcher 3: Wild Hunt" : "PC, PlayStation, Xbox, Switch",
    "Animal Crossing: New Horizons" : "Nintendo Switch",
    "Cyberpunk 2077" : "PC, PlayStation, Xbox",
}

# 2
print(video_game_platforms_dict)

# 3
print("The platform of the 2nd Video game is ",["God of war"])
      
# 4
video_game_platforms_dict["Red Dead Redemption"] = ['Computer']

# 5
del video_game_platforms_dict["Call of Duty: Warzone"]
 
# 2 
print(video_game_platforms_dict)

# 6
last_key = list(video_game_platforms_dict.keys())[-1]
last_value = video_game_platforms_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)