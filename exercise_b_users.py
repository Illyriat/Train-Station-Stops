from cgi import print_directory


users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake",
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users['Jonathan'] ['twitter'])


# 2. Get Erik's hometown
print(users['Erik']['home_town'])


# 3. Get the list of Erik's lottery numbers
print(users['Erik']['lottery_numbers'])


# 4. Get the species of Avril's pet Monty
avrils_pets = users['Avril']['pets']
for animal in avrils_pets:
    if animal['name'] == "monty":
        print(animal['species'])

# print(users["Avril"]["pets"][0]["species"])


# 5. Get the smallest of Erik's lottery numbers
eriks_numbers = users['Erik']['lottery_numbers']

eriks_numbers.sort()
print(eriks_numbers[0])

# print(min(users["Erik"]["lottery_numbers"])[0])

# sorted(users['Erik]["lottery_numbers"][0])

# users["Erik"]["lottery_numbers"].sort()[0]


# 6. Return an list of Avril's lottery numbers that are even
avrils_numbers = users['Avril']['lottery_numbers']

for num in avrils_numbers:
    if num % 2 == 0:
        print(num, end=" ")


# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
eriks_numbers = users['Erik']['lottery_numbers']

eriks_numbers.append(7)
print(eriks_numbers)

# users["Erik"]["lottery_numbers"].append(7)


# 8. Change Erik's hometown to Edinburgh
eriks_hometown = users['Erik']['home_town']

eriks_hometown = "Edinburgh"
print(eriks_hometown)

# users["Erik"]["home_town"] = "Edinburgh"


# 9. Add a pet dog to Erik called "fluffy"
eriks_pets = users['Erik']['pets']

new_pet = {
    "name": "fluffy",
    "species": "dog",
}

eriks_pets.append(new_pet)
print(eriks_pets)

# users["Erik"]["pets"].append({"name": "fluffy", "species": "dog"})


# 10. Add another person to the users dictionary
new_user = {
    "James": {
        "twitter": "jimbo",
    }
}
users.update(new_user)
print(users)