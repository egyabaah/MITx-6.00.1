x = float(input("Enter your number here: "))

difference = 0.01
high = x
low = 0
ans = (high+low) / 2.0
count = 0
while abs(ans**2-x) >= difference:
	print("low = " + str(low) + " high = " + str(high))
	count +=1
	if x<0:
		low = 
	elif ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high+low) / 2.0
print("Number of guesses = " + str(count))
print(str(ans) + " is close to square roof of " + str(x))