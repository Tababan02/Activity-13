artist_songs_dict = {
   "Adele" : "Rolling in the Deep",
  "Taylor Swift" : "Shake It Off",
  "Drake" : "God's Plan",
  "Ed Sheeran" : "Shape of You",
  "Beyoncé" : "Crazy in Love",
  "Bruno Mars" : "Uptown Funk",
  "Billie Eilish" : "Bad Guy",
  "Justin Bieber" : "Sorry",
  "Katy Perry" : "Firework",
  "Post Malone" : "Circles",
}
  
# 2
print(artist_songs_dict)

# 3
print("The top song of the 3rd artist is ", "Drake")
      
# 4
artist_songs_dict["Bruno Mars"] = "Thats what i like"

# 5
del artist_songs_dict["Katy Perry"]
 
# 2 
print(artist_songs_dict)

# 6
last_key = list(artist_songs_dict.keys())[-1]
last_value = artist_songs_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)