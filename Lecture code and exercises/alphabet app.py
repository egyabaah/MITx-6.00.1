def text1(text):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	newtext = text.lower()
	ans = ""
	for c in newtext:
		if c.isalpha() == True :
			ans += " " + str(alphabet.index(c) + 1)
	print(ans)
	
text1("We56 go89ing t7o school")