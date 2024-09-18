fruit_colors_dict = {
	"Apple" : "Red",
	"Banana" : "Yellow",
	"Orange" : "Orange",
	"Grapes" : "Green",
	"Lemon" : "Yellow",
	"Strawberry" : "Red",
	"Watermelon" : "Green",
	"Blueberry" : "Blue"
}

# 2
print(fruit_colors_dict)

# 3
print("The color of the 6th fruit is ", ['Watermelon'])

# 4
fruit_colors_dict["Lemon"] = 'White'

# 5
del fruit_colors_dict['Blueberry']

# 2
print("After updating and Deleting ", fruit_colors_dict)

#6
last_key = list(fruit_colors_dict.keys())[-1]
last_value = fruit_colors_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)
