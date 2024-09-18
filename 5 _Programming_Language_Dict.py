programming_language_dict = {
	"Python" : "Guido van Rossum",
	"Java" : "James Gosling and Mike Sheridan at Sun Microsystems",
	"C" : "Dennis Ritchie and Bell Labs",
	"JavaScript" : "Brendan Eich",
	"C++" : "Bjarne Stroustrup",
	"Ruby" : "Yukihiro Matsumoto",
	"PHP" : "Rasmus Lerdof"
	}

# 2 
print(programming_language_dict)

# 3
print("The 4th programming language and the developers is: ", programming_language_dict['C++'])

# 4
programming_language_dict["PHP"] = "SANDARA"

# 5
del programming_language_dict["C"]

# 2 
print(programming_language_dict)

# 6
last_key = list(programming_language_dict.keys())[-1]
last_value = programming_language_dict[last_key]
print("The last key-value is: ", last_key, ":", last_value)