# Control Flow

# The order in which the program makes decisions
# Like giving a Python a recipe or and order to do things

# Conditional statements:
# if and elif

age = input("Who are you?\n"
            "Choose from:\n"
            "Adult\n"
            "Teenage\n"
            "Younger Teenage\n"
            "Kid\n"
            "Baby\n"
            "Type your answer here -->  ")
age = age.lower()


if age == "adult":
    print("You can watch all movies!")
elif age == "teenage":
    print("Sorry tou cannot watch 18 rated movies, but you can watch all other movies")
elif age == "younger teenage":
    print("Sorry tou cannot watch 18 or 15 rated movies, but you can watch all other movies")
elif age == "kid":
    print("Sorry tou cannot watch 18, 15, 12 rated movies, but you can watch all other movies")
elif age == "baby":
    print("You can only watch U rated movies")
else:
    print("I don't even know how old you are")

# There are no case or switch statements in Python


