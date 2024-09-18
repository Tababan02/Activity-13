city_population_dict = {
	"Quezon City": "2,761,720",
	"Manila" : "1,600,000",
	"Caloocan City" : "1,500,000",
	"Davao" : "1,212,504",
	"Cebu City" : "798,634",
	"Taguig" : "644,473",
	"Pasig City" : "617,301",
	"Las Pinas" : "590,000",
	"Antipolo" : "549,543",
	"Makati City" : "510,383" 
}

# 2
print(city_population_dict)

# 3
print("The population of the 6th city is ", city_population_dict['Pasig City'])

# 4
city_population_dict['Davao'] = '1,800,000'

# 5
del city_population_dict["Makati City"]

# 2 
print(city_population_dict)

# 6
last_key = list(city_population_dict.keys())[-1]
last_value = city_population_dict[last_key]
print("The last key-value is ", last_key, ":", last_value)