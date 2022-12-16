def balancecc(balance, annualInterestRate, monthlyPaymentRate):
	for i in range(12):
		balance = (balance - (monthlyPaymentRate*balance)) +  ((balance - (monthlyPaymentRate*balance)) * (annualInterestRate/12 ))
	print("Month", i+1, "Remaining balance:", round(balance,2))
	
	
balancecc(42, 0.2, 0.04)

balancecc(484, 0.2, 0.04)