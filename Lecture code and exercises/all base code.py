def base(num, x):
	num= num
	if num == 0:
		result = "0"
		print("Base", x, "of", num, "is: ", result)
	if num < 0:
		isNeg = True
		num = abs(num)
	else:
		isNeg = False
	result = ""
	count = 0
	while num > 0:
		result = str(num%x) + result
		num = num // x
		count += 1
	if isNeg: 
		result = "-" + result		
	print("Base", x, "of " + str(num1), "is: ", result)
	print("Number of steps = " + str(count))

num = int(input("Enter an integer in base 10 to find its base: "))
num1 = num
print("What base would you like your answer to be.")
x = int(input("Enter an integer between 0 and 10: "))
print(base(num, x))