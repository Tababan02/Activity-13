software_versions_dict = {
    "Windows" : "Windows 11",
    "macOS" : "macOS Ventura",
    "Ubuntu" : "Ubuntu 22.04 LTS",
    "Android" : "Android 13",
    "iOS" : "iOS 16",
    "Microsoft Office" : "Office 2021",
    "Photoshop" : "Adobe Photoshop 2023",
    "Chrome" : "Google Chrome 117",
    "Firefox" : "Mozilla Firefox 117",
    "Visual Studio Code" : "VS Code 1.78"
}
    
    
# 2
print(software_versions_dict)

# 3
print("The version of the 4th software is ", "Galaxy S23")
      
# 4
software_versions_dict["macOS"] = "Version 13"

# 5
del software_versions_dict["iOS"]
 
# 2 
print(software_versions_dict)

# 6
last_key = list(software_versions_dict.keys())[-1]
last_value = software_versions_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)