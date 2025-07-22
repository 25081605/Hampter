def check_string(text):
    if text.startswith("The"):
        return "Found it! LESGOO"
    else:
        return "Nope"
str1 = "The"
str2 = "Thumbsup Lesgo"
str3 = "Theatre is doneee"
print(check_string(str1))
print(check_string(str2))
print(check_string(str3))