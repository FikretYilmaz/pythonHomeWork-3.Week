number = int(input("Pleas Enter a Number: "))
for i in range(2,number):
	if number % i == 0:
		print(number,"is Not Prime")
		break
else:
	print(number,"is Prime")