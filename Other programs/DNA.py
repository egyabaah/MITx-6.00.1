def DNA_strand(dna):
	ans = ""
	for n in dna:
		if n == "T":
			ans += "A"
		elif n == "A":
			ans += "T"
		elif n == "C":
			ans += "G"
		elif n == "G":
			ans += "C"
		else:
			ans += n
	print(ans)

DNA_strand("ATTGC")