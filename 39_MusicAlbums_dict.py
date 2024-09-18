music_albums_dict = {
    "The Dark Side of the Moon" : 1973,
    "Thriller" : 1982,
    "Back in Black" : 1980,
    "Abbey Road" : 1969,
    "Rumours" : 1977,
    "Nevermind" : 1991,
    "21" : 2011,
    "Born to Run" : 1975,
    "Hotel California" : 1976,
    "1989" : 2014

}
# 2
print(music_albums_dict)

# 3
print("The release year of the 3rd album is ", "Back in Black")
      
# 4
music_albums_dict["Born to Run "] = "2000"

# 5
del music_albums_dict["Rumours"]
 
# 2 
print(music_albums_dict)

# 6
last_key = list(music_albums_dict.keys())[-1]
last_value = music_albums_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)