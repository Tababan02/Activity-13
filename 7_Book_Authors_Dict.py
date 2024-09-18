book_authors_dict = {
	"Pride and Prejudice" : "Jane Austen",
	"1984" : "George Orwell",
	"The Great Gatsby" : "F. Scott Fitzgerald",
	"Moby-Dick" : "Herman Melville",
	"To kill a mockingbird" : "Harper Lee",
	"The catcher in the Rye" : "J.D. Salinger",
	"The Adventures of Huckleberry Finn" : "Mark Twain",
	"Brave New World" : "Aldous Huxley",
	"The Picture of Dorian Gray" : "Oscar Wilde",
	"Fahrenheit 451" : "Ray Bradbury",
	"The Odyssey" : "Homer",
	"Frankenstein" : "Mary Shelley"
}

# 2
print(book_authors_dict)

# 3
print("The 5th book is ",book_authors_dict['Fahrenheit 451'])

# 4
book_authors_dict["The catcher in the Rye"] = 'SANDARA'

# 5
del book_authors_dict['Moby-Dick']

# 2
print(book_authors_dict)

# 5
last_key = list(book_authors_dict.keys())[-1]
lat_value = book_authors_dict[last_key]
print("The last key-value is ", last_key, ":" ,last_value)