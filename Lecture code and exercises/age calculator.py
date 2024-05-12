TIME = "2021-07-03"
def calculate_age(dob):
	dob = dob.split("-")
	print("year =", dob[0])
	print("month =", dob[1])
	def age_calc(dob, time):
		year_old = int(time[0]) - int(dob[0])
		month_old = int(time[1]) - int(dob[1])
		day_old = int(time[2]) - int(dob[2])
		year, month, day = year_old, month_old, day_old
		return year, month, day
	time = TIME.split("-")
	b = age_calc(dob, time)
	year = b[0]
	month = b[1]
	day = b[2]
	leap_year = int(time[0]) - 2000
	is_leap = bool(leap_year % 4 ==0)
	print(is_leap)
	print(b[2])
	x = 31
	if set(dob[1]) <= set("09, 04, 06, 10, 9, 4, 6"):
		x = 30
	elif set(dob[1]) <= set("02, 2") and is_leap == True:
		x= 28
		print("Year", dob[0], "is a leap year.")
	elif set(dob[1]) <= set("02, 2") and is_leap == False:
		x= 27
		print("Year", dob[0], "is not a leap year.")
	k = 31
	if set(time[1]) <= set("09, 04, 06, 10, 9, 4, 6"):
		k = 30
	elif set(time[1]) <= set("02, 2") and is_leap == True:
		k = 28
	elif set(time[1]) <= set("02, 2") and is_leap == False:
		k = 27	
	print(x)
	yar = "year"
	if b[0] > 1:
		yar = "years"
	if b[0] == 0:
		yar = "years"
	mnth = "months"
	if b[0] <= 0 and b[1] <= 0 and b[2] <= 0 :
		print("You haven't been born!")
	else:
		if month < 0:
			month = 12 + month
			year -= 1
		if day < 0:
			day = (x + day) + 1
			month -= 1
		if month == 1:
			mnth = "month"
		print("Your age is ", year, yar + ",", month, mnth, "and", day, "days", "old")
	if b[1] == 0 and b[2] == 0:
		print("Happy Birthday!")
	elif year <=0 and month <=0 and day <1:
		print("Nothing")
	else:
		mon = b[1]
		days = b[2]
		if b[1] > 0:
			mon = 12 - b[1]
		elif b[1] < 0:
			mon = abs(b[1])
		if b[2] > 0:
			days = abs[2] - k
		elif b[2]:
			days = abs(b[2]+1)
		print(mon, mnth, "and", days, "days", "remaining for your birthday")
		
		
y = input("Please Enter Your Date Of Birth in YYYY-MM-DD (eg. 2001-10-21: ")
z= y.split("-")
m= z[2] + "-" +  z[1] + "-" + z[0]
print(m)
calculate_age(y)


print("calculate_age(2002-07-04")