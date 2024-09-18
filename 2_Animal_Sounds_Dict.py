animal_sounds_dict = {
	"Cat": "Meow",
	"Dolphin": "click",
	"Zebra": "Whistle",	
	"Rooster": "Cluck",
	"Pig": "Snort" ,
	"Penguin": "Honk",
	"Leopard": "Growl",
	"Alligator": "Hiss"
}

# 2
print(animal_sounds_dict)

# 3
print(animal_sounds_dict["Pig"])
print(animal_sounds_dict["Pig"][1])

# 4
animal_sounds_dict["Alligator"] = 'Swiss'

# 5
del animal_sounds_dict["Penguin"]

# 2 
print(animal_sounds_dict)

# 6
last_key = list(animal_sounds_dict.keys())[-1]
last_value = animal_sounds_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)