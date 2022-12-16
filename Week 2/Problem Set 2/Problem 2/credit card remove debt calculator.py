balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12
low = balance/12
high =(balance*((1.0+ monthlyInterestRate)**12))/12
monthlyPayment = (high+low) / 2
initial_balance = balance
while balance > 0:
	for n in range(12):
		balance  = balance - monthlyPayment
		interest = balance * monthlyInterestRate	
		balance = balance + interest
	if balance <= -0.12:
		high = monthlyPayment
	elif balance > 0:
		low = monthlyPayment
	else:
		break
	balance = initial_balance
	monthlyPayment = (high+low) / 2	
	print(" Lowest Payment:", round(monthlyPayment,2))