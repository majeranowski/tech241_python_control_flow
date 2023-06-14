# for loops and while loops

# for and foreach in other languages
# in Python we just use for loop

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

# for num in list_data:
#     print(num * 2) # 2, 4, 6, 8, 10

# nested loops
# for data in embedded_list:
#     print(data)
#     for num in data:
#         print(num)

# looping through dictionary

# for item in dict_data.values():
#     print(item)

for item in dict_data.values():
    for embedded_value in item.values():
        print(embedded_value)

# a loop that only returns the money
for items in dict_data.values():
    print(items["Money"])

# loops and if statements
print("----------")
# for num in list_data:
#     if num % 2 == 0:
#         print(num, "even")
#     else:
#         print(num, "odd")

# while loops

x = 0

while x < 10:
    print(f"it's working -> {x}")
    x += 1

while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    x += 1

# verifying user input

user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) > 0 and int(age) <= 117:
        user_prompt = False
    else:
        print("You have to enter a digit between 1 - 117")

print(f"Your age is {age}")




