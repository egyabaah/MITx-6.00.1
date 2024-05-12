vowel = "aeoiuAEOIU"
word = input("Enter a word here: ")
times = int(input("Enter a number here: "))
n = 0

while n < len(word):
    char = word[n]
    if char in vowel:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    n += 1
print("What does that spell?")
for c in range(times):
    print(c)
    print(word + "!!!")
