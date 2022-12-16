balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
def balancecc(balance, annualInterestRate, monthlyPaymentRate):
	for i in range(12):
		balance = balance - (monthlyPaymentRate*balance) 
		interest = (annualInterestRate/12)*balance
		balance = (balance + interest)
	print("Month", i+1, "Remaining balance:", round(balance,2))
	
	
balancecc(42, 0.2, 0.04)

balancecc(484, 0.2, 0.04)