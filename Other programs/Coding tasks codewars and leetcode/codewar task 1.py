import string

low_alph = string.ascii_lowercase
list1 = []
for i in low_alph:
	position = low_alph.find(i) + 3
	if position > 25:
		position -= 26
	list1.append(i)
	list1.append(low_alph[position])
encoder_dict = dict((list1[i], list1[i+1]) for i in range(0, len(low_alph), 2))
	
print(list1)
print(encoder_dict)