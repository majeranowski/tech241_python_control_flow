# Control flow and loops

### Control flow

The order in which the program makes decisions

Like giving a Python a recipe or and order to do things

##### Conditional statements:
##### if and elif

In Python there is no switch or case statements

Example of the program that gives a feedback about movie rating depending on your age:

```python
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
```

### Loops
##### For loops

In python there is only for loop. No foreach

Iterating over different collections:

```python
list_data = [1, 2, 3, 4, 5]
embedded_list = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"Name": "Bronson",
        "Money": "$0.05"},
    2: {"Name": "Masha",
        "Money": "$3.66"},
    3: {"Name": "Roscoe",
        "Money": "$1.14"}
}

for num in list_data:
     print(num * 2) # 2, 4, 6, 8, 10

# nested loops
 for data in embedded_list:
     print(data)
     for num in data:
         print(num)

# looping through dictionary

 for item in dict_data.values():
     print(item)

for item in dict_data.values():
    for embedded_value in item.values():
        print(embedded_value)

# a loop that only returns the money
for items in dict_data.values():
    print(items["Money"])

# loops and if statements
print("----------")
for num in list_data:
    if num % 2 == 0:
        print(num, "even")
    else:
        print(num, "odd")
```

##### While loops

While loop will run while condidion is True.

```python
x = 0

while x < 10:
    print(f"it's working -> {x}")
    x += 1

while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    x += 1

verifying user input

user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) > 0 and int(age) <= 117:
        user_prompt = False
    else:
        print("You have to enter a digit between 1 - 117")

print(f"Your age is {age}")

```