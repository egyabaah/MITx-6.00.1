x = float(input("Enter an integer to find its cube root: "))
epilson = 0.01
guess = 0
count = 0
increment = 0.00001
if x > 0:
	print("Would you like to use your own increment value?")
	option = input("Type Yes or No (Type No if you are unsure): ")
	n = 0
for n in range(len(option)):
		if option[n] == "y" or option[n:n+3] == "yes" or option[n:n+3] == "ye" or option[n] == "Y" or \
				option[n:n+3] == "YES" or option[n:n+3] == "YE" or option[n:n+3] == "Yes" or option[n:n+3] == "YE":
			user_increment = float(input("Enter your increment value which should be less than 0.01: "))
			increment = user_increment
		else:
			increment
while abs(guess**3-x) >= epilson:
	guess += increment
	count += 1
if guess**3 >= x:
		print("Failed on cube root of", x)
else:
		print ("number of guesses =" + str(count))
		print(guess, "is close to cube root of", x)
	