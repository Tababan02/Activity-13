university_courses_dict = {
	"Harvard University": "Law, Economics",
	"Stanford University": "Psychology",
	"MIT": "Engineering",
	"UC Berkeley": "Environmental Science",
	"Oxford": "Philosophy, Literature",
	"Cambridge": "Mathematics, Engineering",
	"Columbia": " Business",
	"University of Chicago" : "Economics Law",
	"Yale": "Drama, History,",
	"Caltech": "Astrophysics"
}

# 2
print(university_courses_dict)

# 3
print("The course of the 3rd university is ", university_courses_dict["UC Berkeley"])

# 4
university_courses_dict["Cambridge"] = "BSIT"

# 5
del university_courses_dict["University of Chicago"]

# 2
print(university_courses_dict)

# 6
last_key = list(university_courses_dict.keys())[-1]
last_value = university_courses_dict[last_key]
print("The last value-key pair is ", last_key, ":", last_value)	