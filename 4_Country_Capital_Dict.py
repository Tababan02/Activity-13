 country_capital_dict = {
	"Russia" : "Moscow",
	"United Kingdom" : "London",
	"Germany" : "Berlin",
	"Spain" : "Madrid",
	"Ukraine" : "Kiev",
	"Italy" : "Rome",
	"France" : "Paris",
	"Belarus" : "Minsk",
	"Austria" : "Vienna",
	"Romania" : "Bucharest",
	"Poland" : "Warsaw", 
	"Hungary" : "Budapest" 
}

# 2
print(country_capital_dict)

# 3
print("The capital of the 5th country is ",country_capital_dict['Italy'])

# 4
country_capital_dict["Austria"] = "Manila"

# 5
del country_capital_dict["Hungary"]

# 2
print(country_capital_dict)

# 6
last_key = list(country_capital_dict.keys())[-1]
last_value = country_capital_dict[last_key]
print("The last key-value is: ", last_key, ":",last_value)

