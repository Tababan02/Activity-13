festival_dates_dict = {
    "New Year's Day" : "January 1",
    "Diwali" : "October or november",
    "Christmas" : "December 25",
    "Eid al-Fitr" : "August",
    "Thanksgiving" : "November 19",
    "Halloween" : "October 31",
   "Holi" : "March 25",
    "Chinese New Year" : " January or February",
    "Oktoberfest" : "October 6",
    "Valentine's Day" : "February 14"

}   
    
    
# 2
print(festival_dates_dict)

# 3
print("The date of the 3rd festival is ", "Christmas")
      
# 4
festival_dates_dict["Holi"] = "September 13"

# 5
del festival_dates_dict["Thanksgiving"]
 
# 2 
print(festival_dates_dict)

# 6
last_key = list(festival_dates_dict.keys())[-1]
last_value = festival_dates_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)