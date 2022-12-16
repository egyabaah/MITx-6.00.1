# Sum of all numbers preceeding a number
total=0
end=6
while end>0:
   total+=end
   end-=1
print("total" + str(total))

# Print all multiples of 5 and 3 below 100
total3=0
total= 0
for i in range(1, 100):
  a = str(i)
  if i%3 == 0 or i%5==0:
    a= str(i)
    total3+=1
    total= total, str(i)
    print(a)
    print("Multiples of 3 and 5= ", i)      
print("Multiples of 3 and 5= ", total)       
print("Number of Multiples of 3 and 5 from 1-100= ", total3)   
    
 
total3=0
total= 0
for i in range(1, 100):
  a = str(i)
  if i%3 == 0 or i%5==0:
    b= i
    while True:
      print(b)
      


# Print number of vowels in a wor
s = "azcbobobegghakl"
total4 = 0
vowels = {"a", "e", "i", "o", "u"}
for g in range(s):
	if g in vowels:
		total4 += 1
print("Number of Vowels is:" + str(total4))
