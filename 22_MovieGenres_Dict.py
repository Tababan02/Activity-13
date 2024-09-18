movie_genres_dict = {
    "Action" : "Mad Max: Fury Road",
    "Comedy" : "Superbad",
    "Drama" : "The Shawshank Redemption",
    "Horror" : "Get Out",
    "Science Fiction" : "Inception",
    "Romance" : "The Notebook",
    "Thriller" : "Se7en",
    "Fantasy" : "The Lord of the Rings: The Fellowship of the Ring",
}

# 2
print(movie_genres_dict)

# 3
print("the example movie of the 3rd genre is ",["Drama"])
      
# 4
movie_genres_dict["Science Fiction"] = ['Arrival']

# 5
del movie_genres_dict["Thriller"]
 
# 2 
print(movie_genres_dict)
# 6

last_key = list(movie_genres_dict.keys())[-1]
last_value = movie_genres_dict[last_key]
print("The last key-value pair is ", last_value, ":",last_key)