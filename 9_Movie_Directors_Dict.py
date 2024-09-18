movie_directors_dict = {
	"Inception" : "Christopher Nolan",
	"The Godfather" : "Francis Ford Coppola",
	"Pulp Fiction" : "Quentin Tarantino",
	"Schindler's List" : "Steven Spielberg",
	"The Shawshank Redemption" : "Frank Darabont",
	"The Dark Knight" : "Christopher Nolan",
	"Forrest Gump" : "Robert Zemeckis",
	"Fight Club" : "David Fincher",
	"Interstellar" : "Christopher Nolan",
	"Get Out" : "Jordan Peele"
	}

# 2 
print(movie_directors_dict)

# 3
print("The director of the 5th movie is ", ['The Dark Knight'])

# 4
movie_directors_dict["Get Out"] = 'SANDARA'

# 5
del movie_directors_dict["Fight Club"]

# 2 
print(movie_directors_dict)

# 6
last_key = list(movie_directors_dict.keys())[-1]
last_value = movie_directors_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)