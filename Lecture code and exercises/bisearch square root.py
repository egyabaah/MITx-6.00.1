x = float(input("Enter your number here: "))

epilson = 0.01
high = x
low = 0
ans = (high + low) / 2
count = 0
print("Would you like to use your own error rate of tolerance value")
option = input("Type Yes or No (Type No if you are not sure): ")
for n in range(len(option)):
    if option[n:] == "yes" or option[n:n + 2] == "ye" or option[n] == "y" or option[n:] == "Yes" or \
            option[n:n + 2] == "Ye" or option[n] == "Y" or option[n:] == "YES" or option[n:n + 2] == "YE":
        user_epilson = float(input("Type your error rate of tolerance value which should be an integer less than 0: "))
        epilson = user_epilson
if x < 1:
    high = 1
    low = x
    ans = (high + low) / 2
    while abs(ans ** 2 - x) >= epilson:
        print("low = " + str(low) + ", high" + str(high))
        count += 1
        print("epilson=", epilson)
        if ans ** 2 < x:
            low = ans
        else:
            high = ans

        ans = (high + low) / 2

else:
    high = x
    low = 0
    ans = (high + low) / 2
    while abs(ans ** 2 - x) >= epilson:
        count += 1
        print("low= ", low, " and ", "high =", high)
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2

print("Number of guesses", count)
print(ans, "is close to square root of ", x)
