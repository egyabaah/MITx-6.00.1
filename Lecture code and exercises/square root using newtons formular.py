epilson = 0.01
x= 24
guess = x/2.0
numGuesses = 0

while abs(guess**2 - x) >= epilson:
	numGuesses +=1
	guess = guess - (((guess**2)-x)/(2*guess))
print("NumGuesses = " + str(numGuesses))
print("Square root of " + str(x) + " is about " + str(guess))