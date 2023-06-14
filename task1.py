while True:
    age_str = input("Enter your age: ")

    if age_str.isdigit():
        age = int(age_str)

        if age < 1 or age > 117:
            print("Invalid age. Please enter a valid age between 1 and 117.")
        else:
            if age >= 18:
                print("You can watch all rated movies.")
            elif age >= 15:
                print("You can watch U, PG, 12, and 15 rated movies.")
            elif age >= 12:
                print("You can watch U, PG, and 12 rated movies.")
            elif age >= 1:
                print("You can watch U and PG rated movies.")

            break
    else:
        print("Invalid input. Please enter a valid age as a number.")

print("Thank you!")
