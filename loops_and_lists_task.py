"""
Make a loop with a range that says hello 10 times (research range please)

Create another loop with a range that asks for names and appends to a list called list_names

Make a loop that iterates over each name in list_name and format's it into lowercase in a new list called list_names_lower

Make a list of numbers, iterate over the list of values to find if they are even. Print the even numbers.
"""
# task 1
# for i in range(1,11):
#     print("Hello")

#task 2 and 3

# list_names = []
#
# num_names = int(input("Enter the number of names: "))
#
# for i in range(num_names):
#     name = input("Enter a name: ")
#     list_names.append(name)
#
# print("List of names:", list_names)
#
# list_names_lower = []
#
# for name in list_names:
#     lowercase_name = name.lower()
#     list_names_lower.append(lowercase_name)
#
# print("list of lowercase names:", list_names_lower)

#task 4

# list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for even in list_of_numbers:
#     if even % 2 == 0:
#         print(even)

#extra tasks
# sum = 0
# for i in range(0,101):
#     sum += i
# print(sum)

odd_sum = 0
even_sum = 0

for i in range(0,101):
     if i % 2 == 0:
         even_sum += i
     else:
         odd_sum += i
print("summary of odd numbers is: ", odd_sum)
print("summary of even numbers is: ", even_sum)
