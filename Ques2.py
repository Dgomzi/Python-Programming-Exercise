#!/usr/bin/python3

def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

print(",".join([str(factorial(int(n))) for n in input("Enter the number be factorialised separated by comma ").split(",")]))

