car_specs_dict = {
   "Tesla Model S" : "Horsepower: 670, Top Speed: 200 mph, Range: 405 miles",
  "Ford Mustang" : "Horsepower: 450, Top Speed: 155 mph", "Engine": "5.0L V8",
  "Chevrolet Corvette" : "Horsepower: 495, Top Speed: 194 mph, Engine: 6.2L V8",
  "Toyota Camry" : "Horsepower: 203, Top Speed: 130 mph, Fuel Economy: 28 mpg city / 39 mpg highway",
  "Honda Accord" : "Horsepower: 192, Top Speed: 130 mph, Fuel Economy: 30 mpg city / 38 mpg highway",
  "BMW M3" : "Horsepower: 473, Top Speed: 155 mph, Engine: 3.0L I6",
"Mercedes-Benz C-Class" : "Horsepower: 255, Top Speed: 130 mph, Engine: 2.0L I4",
  "Subaru Outback" : "Horsepower: 182, Top Speed: 130 mph, AWD: Yes",
  "Volkswagen Golf" : "Horsepower: 228, Top Speed: 155 mph, Fuel Economy: 28 mpg city / 36 mpg highway",
  "Audi A4" : "Horsepower: 201, Top Speed: 130 mph, Engine: 2.0L I4" 
}
  
# 2
print(car_specs_dict)

# 3
print("The specification of the 4th car model are ", "Toyota Camry")
      
# 4
car_specs_dict["Volkswagen Gold"] = "Horsepower: 228, Top Speed: 155 mph, Fuel Economy: 30 mpg city / 40 mpg highway"

# 5
del car_specs_dict["Honda Accord"]
 
# 2 
print(car_specs_dict)

# 6
last_key = list(car_specs_dict.keys())[-1]
last_value = car_specs_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)