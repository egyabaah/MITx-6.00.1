cube = float(input("Enter the number you want to find it's square root: "))
difference = 0.00001
guess = 0
increment = 0.001
input2 = False
if cube > 0:
    print("Would you like to use your own increment")
    option = input("Type Yes or No (type No if you are not sure): ")
    n = 0
    b = option
    print(b)
for n in range(len(option)):
    if option[n:n + 3] == "y" or "ye" or "yes":
        user_increment = float(input("Type your increment value which should be an integer less than 0: "))
        increment = user_increment
        print(increment)
        break
    else:
        print("False")
