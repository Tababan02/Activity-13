beaches_countries_dict = {
  "Copacabana Beach" : "Brazil",
  "Bondi Beach" : "Australia",
  "Waikiki Beach" : "USA",
  "Playa del Carmen" : "Mexico",
  "Phra Nang Beach" : "Thailand",
  "Whitehaven Beach" : "Australia",
  "Anse Source d'Argent" : "Seychelles",
  "Malibu Beach" : "USA"
}

# 2
print(beaches_countries_dict)

# 3
print("the country of the 3rd beach is ", "Waikiki Beach")
      
# 4
beaches_countries_dict["Whitehaven Beach"] = "Philippines"

# 5
del beaches_countries_dict["Phra Nang Beach"]
 
# 2 
print(beaches_countries_dict)

# 6
last_key = list(beaches_countries_dict.keys())[-1]
last_value = beaches_countries_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)