"""
Here are some programs to make. Each should use a While loop.

Take 10 integers from the user and print their average value once you have them all

Write a while loop to print the following series:10, 20 ,30, 40 etc. up to 300

Upgrade your waiter program to only allow items from the menu to be entered

Write a program that takes user input until the user enters 0. Once they do, sum all the positive numbers they entered and all of the negative numbers they entered and print the result back to them.

"""
# task 1
# counter = 0
# sum = 0
# while counter < 10:
#     num = int(input("Give me a number: "))
#     sum += num
#     counter += 1
# print("Avarage of the numbers you provided is: ", sum/10)

# task 2

# counter = 10
# while counter <= 300:
#     print(counter)
#     counter += 10

# task 3
#
# # creating a menu list
# menu = ['burata', 'tartare', 'salad','salmon', 'chicken', 'duck', 'strudel', 'cheesecake', 'cherry pie']
# # creating an empty list for client order
#
# client_order = []
# #variable controlling a loop
# loop = True
# # while loop to ask for a user input
# while loop:
#     print("What would you like to do ? \n"
#       "1. See the menu\n"
#       "2. Order\n"
#       "3. See my order\n"
#       "4. Finish")
#     choice = int(input("choose: "))
# # if statements for different inputs
#     if choice == 1:
#         print(menu)
#     elif choice == 2:
#         order = input("Enter your order: ")
#         if order in menu:
#             print("Order accepted")
#             client_order.append(order)
#         else:
#             print("Item is not on the menu, try again")
#     elif choice == 3:
#      print(client_order)
#     else:
#         loop = False

# task 4

positive_sum = 0
negative_sum = 0

while True:
    user_input = int(input("Enter a number (enter 0 to exit): "))

    if user_input == 0:
        break

    if user_input > 0:
        positive_sum += user_input
    else:
        negative_sum += user_input

print("Sum of positive numbers:", positive_sum)
print("Sum of negative numbers:", negative_sum)
