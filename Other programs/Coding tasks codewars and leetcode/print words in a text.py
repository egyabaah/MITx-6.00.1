def task(text):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	return " " .join(str(alphabet.index(c)+ 1) for c in text.lower() if c.isalpha())
	
print(task("We56 go89ing t7o school"))