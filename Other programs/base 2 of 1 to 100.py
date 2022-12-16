for num in range(100):
	num1 = num
	if num < 0:
		isNeg = True
		num = abs(num)
	else:
		isNeg = False
	result = " "
	count = 0
	if num == 0:
		result = "0"
	while num > 0:
		result = str(num%2) + result
		num = num // 2
		count += 1
	if isNeg:
		result = "-" + result
	print("Base two of " + str(num1) + " is: " + result)
	print("Number of steps = " + str(count))