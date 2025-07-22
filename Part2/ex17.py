import random

name = input("What's your name??\n")

characters = ["GIYUU", "LEVI", "LUFFY", "TANJIRO"]
picked_code = random.choice(characters)

adjectives = ["BRAVE", "HANDSOME", "COOL", "KIND"]
picked_adjective = random.choice(adjectives)

print(name, "your code name is " + picked_adjective +" " + picked_code, "!!")

number = random.randint(1, 99)
print("Your lucky number isss", number, "!!")



# Fixed line below: replaced picked_characters with picked_code


