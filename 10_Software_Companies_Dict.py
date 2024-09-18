software_companies_dict = {
	"Microsoft": "Redmond, Washington, USA",
	"Apple": "Cupertino, California, USA",
	"Google (Alphabet Inc.)": "Mountain View, California, USA",
	"Oracle": "Austin, Texas, USA",
	"SAP": "Walldorf, Germany",
	"IBM": "Armonk, New York, USA",
	"Salesforce": "San Francisco, California, USA",
	"Adobe": "San Jose, California, USA",
	"Intuit": "Mountain View, California, USA",
	"VMware": "Palo Alto, California, USA"
}

# 2
print(software_companies_dict)

# 3
print("The headquarters of the 3rd company is: ", ['Oracle'])

# 4
software_companies_dict["Intuit"] = 'Manila'

# 5
del software_companies_dict['VMware']

# 2 
print(software_companies_dict)

# 6
last_key = list(software_companies_dict.keys())[-1]
last_value = software_companies_dict[last_key]
print("The last key-value is ",last_key, ":", last_value)