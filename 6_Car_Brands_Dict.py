car_brands_dict = {
	"Toyota" : "Japan",
	"Ford" : "United States",
	"Honda" : "Japan",
	"BMW" : "Germany",
	"Mercedes-Benz" : "Germany",
	"Nissan" : "Japan",
	"Hyundai" : "South Korea",
	"Subaru" : "japan",
	"Audi" : "Germany",
	"Tesla" : "United States"
	}

# 2
print(car_brands_dict)

# 3
print("3rd car brand is: ", car_brands_dict['BMW'])

# 4
car_brands_dict["Subaru"] = 'Philippines'

# 5
del car_brands_dict['Audi']

# 2
print(car_brands_dict)

# 6
last_key = list(car_brands_dict.keys())[-1]
last_value = car_brands_dict[last_key]
print("The last key-value is : " ,last_key, ":", last_value)