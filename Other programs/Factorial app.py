def fact(x):
	if x == 1:
		return 1
	else:
		return x*(fact(x-1))
		
print(fact((int(input("Enter a number here to find its factorial: ")))))