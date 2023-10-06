def add(n1,n2):
	for i in range(1,n2+1):
		n1+=1
	return n1

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))

print(add(num1,num2))