x = float(input("Enter the number you want to find it's square root: "))
difference = 0.00001
guess = 0
increment = 0.001
number_of_guesses = False
if x > 0:
    print("Would you like to use your own increment")
    option = input("Type Yes or No (type No if you are not sure): ")
    n = 0
for n in range(len(option)):
    increment = 0.0001
    guess = 0
    difference = 0.01
    if option[n:] == "yes" or option[n:n + 2] == "ye" or option[n] == "y" or option[n:] == "Yes" or option[
                                                                                                    n:n + 2] == "Ye" \
            or option[n] == "Y" or option[n:] == "YES" or option[n:n + 2] == "YE":
        user_increment = float(input("Type your increment value which should be an integer less than 0: "))
        increment = user_increment
        break
    else:
        increment

while abs(guess ** 2 - x) >= difference:
    guess += increment
    number_of_guesses += 1

if guess ** 2 == x:
    print("Failed on cube root of", x)

else:
    print(guess, "is close to cube root of", x)
    print("Number of guesses = " + str(number_of_guesses))
