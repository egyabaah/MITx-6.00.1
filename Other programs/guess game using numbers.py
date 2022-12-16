x = int(input("Please think of a number between 0 and 100!: "))
# print("Please think of a number between 0 and 100!")
high = 100
low = 0
ans = int((high + low) / 2)
option = "no"
if option != "c":
    option = "n"
    for n in range(len(option)):
        b = range(1)
        while len(option) > 2 or option[n] != "c":
            print("Is your secret number " + str(int(ans)) + "?")
            option = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too "
                           "low. \nEnter 'c' to indicate I guessed correctly.")
            if option[n] == "l":
                low = int(ans)
            elif option[n] == "h":
                high = int(ans)
            elif len(option) < 2 and option[n] == "c":
                print("Game over. Your secret number was: ", int(ans))
            else:
                print("Sorry, I did not understand your input.")
            ans = (high + low) / 2
