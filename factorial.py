#!/usr/bin/python3
import sys

def factorial(n):
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result

# Check if an argument was actually provided
if len(sys.argv) < 2:
	print("Usage: python script.py <number>")
	sys.exit(1)

try:
	# Try to convert the argument to an integer
	number = int(sys.argv[1])

	# Factorials aren't defined for negative numbers
	if number < 0:
		print("Please provide a positive integer.")
	else:
		f = factorial(number)
		print(f"The factorial of {number} is {f}")

except ValueError:
	print("Error: Please provide a valid integer.")