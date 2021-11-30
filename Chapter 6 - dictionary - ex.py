info = {
    "First_name": "Lee",
    "Last_name":  "Yung",
    "age": 20,
    "city": "tokyo"

    }
print(info)


favorite_numbers = {"meggie": 15,
"megan": 20,
"louse": 55,
"court": 111,
"kate": 2022,
}
num = favorite_numbers["meggie"]
print("Meggie's favorite number is " + str(num) + ".")
num = favorite_numbers["megan"]
print("Megan's favorite number is " + str(num) + ".")
num = favorite_numbers["megan"]
print("Louse's favorite number is " + str(num) + ".")
num = favorite_numbers["megan"]
print("Court's favorite number is " + str(num) + ".")
num = favorite_numbers["megan"]
print("Kate's favorite number is " + str(num) + ".")

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

word = 'string'
print("\n" + word.title()+": " + glossary[word])
word = 'comment' 
print('\n'+ word.title()+ ': ' +  glossary[word])
word = 'list'
print("\n" + word.title()+ ': ' + glossary[word])
word = 'loop'
print('\n' + word.title()+ ': ' + glossary[word])
word = 'dictionary'
print('\n' + word.title()+ ': ' + glossary[word])

favorite_languages = {
    "jacob": "C++",
    "lindsay": "Java",
    "meredith": "C#" "CSS",
    "jane": "ruby",
}
print("The following languages have been mentioned:")
for favorite_language in favorite_languages.values():
    print(favorite_language.title())

rivers = {
    "nile": "Egypt",
    "amazon": "Brazil",
    "mtkvari": "Tbilisi",
}

for river, location in rivers.items():
    print("The " + river.title() + " runs throgh " + location.title())

for river in rivers.keys():
    print("This is the name of river>>>" + river.title())
for location in rivers.values():
    print("Location: " + location.title())

favorite_languages = {
    "jacob": "C++",
    "lindsay": "Java",
    "meredith": "C# " "CSS",
    "jane": "ruby",
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title()+ ".")


favorite_languages_poll = [
    "loran",
    "jacob",
    "lindsay",
    "harry",
    "jefrey",
]

for poller in favorite_languages_poll:
    if poller in favorite_languages.keys():
        print("Thank you for responding " + poller.title()+ " !")
    else:
        print("Greetly inviting " + poller.title() + " to take the poll.")

info = {
    "First_name": "Lee",
    "Last_name":  "Yung",
    "age": 20,
    "city": "tokyo"
}

info_1 = {
    "First_name": "Lucas",
    "Last_name": "Vasces",
    "age": 25,
    "city": "london"
}
info_2 = {
    "First_name": "Cara",
    "Last_name": "Puentes",
    "age": 18,
    "city": "brussel"
}

people = [info,info_1,info_2]
for inf in people:
    print(inf)

called_pets = []

pet = {
    "Pet type": "dog",
    "Pet owner": "James martens"
}
called_pets.append(pet)
pet = {
    "Pet type": "cat",
    "Pet owner": " Mathis de light"
    }
called_pets.append(pet)

print(called_pets)
for pet in called_pets:
    print("Here is the information about type and owner:")
    for key,value in pet.items():
        print("\t" + key + ": " + value)
    

favorite_places = {
    "liza": ["hawai","california","guatemala"],
    "andrew": ["greenland","bali","honduras"],
    "bill": ["portland","nevada","paraguay"]
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s wondering places:")
    for place in places:
        print("\t"+ place.title())

favorite_numbers = {
    "may": [1,22,222],
    "jule": [1000,2000,3000],
    "megan": [7,14,21]
}
for k, vs in favorite_numbers.items():
    print("List of " + k.title() + "'s favorite numbers")
    for v in vs:
        print(" - Number:" + str(v))

countries = {
    "england": {
        "capital city": "london",
        "population": 8980000,
        "sightseeings": "big-ben" + "london eye.",
    },
    "italy": {
        "capital city": "rome",
        "population": 287300,
        "sightseeings": "colloseum" + "pompei.",
    },
    "brazil": {
        "capital city": "brazil",
        "population": 4291577,
        "sightseeings": "ipanema beach.",
    }}


for country, country_info in countries.items():
    city = country_info["capital city"].title()
    population = country_info["population"]
    sightseeings = country_info["sightseeings"]

    print("\n" + country.title() + "'s city is " + city.title())
    print("It has about population "+ str(population))
    print("It has some of favorite sightseeings: " + sightseeings )


