sports_players_dict = { 
		"Soccer": "Pelé",
		"Basketball": "Michael Jordan",
		"Tennis": "Serena Williams",
		"Golf": "Tiger Woods",
		"American Football": "Tom Brady",
		"Baseball": "Babe Ruth",
		"Hockey": "Wayne Gretzky",
		"Cricket": "Sachin Tendulkar",
		"Boxing": "Muhammad Ali",
		"Rugby": "Richie McCaw"
}


# 2 
print(sports_players_dict)

# 3
print("The player of the 4th sports is: ",sports_players_dict["American Football"])

# 4
sports_players_dict['Hockey'] = "SANDARA"

# 5
del sports_players_dict['Rugby']

# 2
print(sports_players_dict)

# 6
last_key = list(sports_players_dict.keys())[-1]
last_value = sports_players_dict[last_key]
print("The last key-value pair is: ", last_key , ":", last_value)
