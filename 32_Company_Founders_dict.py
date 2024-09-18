company_founders_dict = {
    "Apple" : "Steve Jobs, Steve Wozniak, Ronald Wayne",
    "Microsoft" : "Bill Gates, Paul Allen",
    "Amazon" : "Jeff Bezos",
    "Google" : "Larry Page, Sergey Brin",
    "Facebook" : "Mark Zuckerberg, Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, Chris Hughes",
    "Tesla" : "Elon Musk, JB Straubel, Martin Eberhard, Marc Tarpenning, Ian Wright",
    "Alibaba" : "Jack Ma",
    "IBM" : "Charles Ranlett Flint",
}   
    
# 2
print(company_founders_dict)

# 3
print("Thefounder of the 6th company is ", "Tesla")
      
# 4
company_founders_dict["Microsoft"] = "SANDARA"

# 5
del company_founders_dict["IBM"]
 
# 2 
print(company_founders_dict)

# 6
last_key = list(company_founders_dict.keys())[-1]
last_value = company_founders_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)