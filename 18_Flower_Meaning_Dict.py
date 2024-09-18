flower_meanings_dict = {
  "Rose" : "Love and passion",
  "Lily" : "Purity and renewal",
  "Tulip" : "Perfect love",
  "Daisy" : "Innocence and purity",
  "Sunflower" : "Adoration and loyalty",
  "Orchid" : "Beauty and strength",
  "Chrysanthemum" : "Friendship and joy",
  "Peony" : "Romance and prosperity"
} 
# 2
print(flower_meanings_dict)

# 3
print("The meaning of the 5th flower is ",['Orchid'])

# 4 
flower_meanings_dict["Peony"] = 'Love'

# 5
del flower_meanings_dict["Chrysanthemum"]

# 2
print(flower_meanings_dict)

# 7
last_key = list(flower_meanings_dict.keys())[-1]
last_value = flower_meanings_dict[last_key]
print("The last key-value pair is " , last_key, ":", last_value)