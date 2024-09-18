currency_symbols_dict = {
    "US Dollar" : "$",
    "Euro" : "€",
    "British Pound" : "£",
    "Japanese Yen" : "¥",
    "Swiss Franc" : "CHF",
    "Canadian Dollar" : "C$",
    "Australian Dollar" : "A$",
    "Chinese Yuan" : "¥",
    "Indian Rupee" : "₹",
    "Brazilian Real" : "R$",
}
# 2
print(currency_symbols_dict)

# 3
print("The symbol of the 5th currency is",["Swiss Franc"])
      
# 4
currency_symbols_dict["Indian Rupee"] = ['&']

# 5
del currency_symbols_dict["British Pound"]
 
# 2 
print(currency_symbols_dict)

# 6
last_key = list(currency_symbols_dict.keys())[-1]
last_value = currency_symbols_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)