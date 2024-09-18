space_telescope_missions_dict = {
  "Hubble Space Telescope" : "Deep space observation.",
  "Chandra X-ray Observatory" : "X-ray study of high-energy regions.",
  "Kepler Space Telescope" : "Exoplanet search.",
  "James Webb Space Telescope" : "Infrared observation of stars and galaxies.",
  "Spitzer Space Telescope" : "Infrared study of celestial objects."
} 

# 2
print(space_telescope_missions_dict)

# 3
print("The missopm of the 1st Telescope is ", "Hubble Space Telescope")
      
# 4
space_telescope_missions_dict["Hubble Space Telescope"] = "Magnify"

# 5
del space_telescope_missions_dict["James Webb Space Telescope"]
 
# 2 
print(space_telescope_missions_dict)

# 6
last_key = list(space_telescope_missions_dict.keys())[-1]
last_value = space_telescope_missions_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)