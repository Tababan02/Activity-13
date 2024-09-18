company_ceos_dict = {
    "Apple": "Tim Cook",
    "Microsoft": "Satya Nadella",
    "Amazon": "Andy Jassy",
    "Google (Alphabet Inc.)": "Sundar Pichai",
    "Facebook (Meta Platforms, Inc.)": "Mark Zuckerberg",
    "Tesla": "Elon Musk",
    "Berkshire Hathaway": "Warren Buffett",
    "IBM": "Arvind Krishna",
    "Oracle": "Safra Catz",
    "Coca-Cola": "James Quincey",
}

# 2
print(company_ceos_dict)

# 3
print("The CEO of the 6th company ",company_ceos_dict["Berkshire Hathaway"])

# 4
company_ceos_dict["Google"] = "Sandara"

# 5
del company_ceos_dict['Coca-Cola']

# 2 
print(company_ceos_dict)

# 6
last_key = list(company_ceos_dict.keys())[-1]
last_value = company_ceos_dict[last_key]
print("The last key-value pair is ", last_value, ":" ,last_key)