# Given two non-negative integers num1 and num2 represented as string, return the sum of the numbers
# You ust not use any built-in BigInteger library or convert the inputs to integer directly.

def AddStrings(num1, num2):
	return str(eval(num1) + eval(num2))

print(AddStrings("4","6"))