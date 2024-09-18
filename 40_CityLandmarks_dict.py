city_landmarks_dict = {
  "Paris" : "Eiffel Tower",
  "New York" : "Statue of Liberty",
  "Rome" : "Colosseum",
  "London" : "Big Ben",
  "Tokyo" : "Tokyo Tower",
  "Sydney" : "Sydney Opera House",
  "Dubai" : "Burj Khalifa",
  "Cairo" : "Pyramids of Giza"
}
# 2
print(city_landmarks_dict)

# 3
print("The landmark of the 6th city is ", "Sydney")
      
# 4
city_landmarks_dict["New York"] = "SUMMIT one"

# 5
del city_landmarks_dict["Dubai"]
 
# 2 
print(city_landmarks_dict)

# 6
last_key = list(city_landmarks_dict.keys())[-1]
last_value = city_landmarks_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)