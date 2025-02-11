import sys

def sum(A, B):
	print(f"Sum:\t\t{A + B}")
def difference(A, B):
	print(f"Difference:\t{(A - B)}")
def product(A, B):
	print(f"Product:\t{(A * B)}")
def quotient(A, B):
	if (B == 0):
		print("Quotient:\tERROR (division by zero)")
		return
	else:
		print(f"Quotient:\t{(A / B)}")
def remainder(A, B):
	if (B == 0):
		print("Remainder:\tERROR (modulo by zero)")
		return
	else:
		print(f"Remainder:\t{(A % B)}")

def main():
	if len(sys.argv) == 1:
		print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
		return
	if len(sys.argv) > 3 :
		print("Error: too many arguments")
		return
	try:
		A = int(sys.argv[1])
		B = int(sys.argv[2])
	except ValueError:
		print("AssertionError: only integers")
		return

	sum(A, B)
	difference(A, B)
	product(A, B)
	quotient(A, B)
	remainder(A, B)
	
if __name__ == "__main__": 
	main()