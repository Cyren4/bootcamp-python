import sys

def	good_way():
	print("Usage: python operations.py <number1> <number2>")
	print("Example:\n\tpython operations.py 10 3")

def	check_digit(argv):
	for param in argv:
		if not param.isdigit():
			return False
	return True

def	check_param(argv):
	if len(argv) != 2:
		if len(argv) < 2 and len(argv) != 0:
			print("InputError: not enough arguments")
		elif len(argv) != 0:
			print("InputError: too many arguments")
		return (False)
	elif not check_digit(argv):
		print("InputError: only numbers")
		return (False)
	return (True)


def	operation(argv):
	if check_param(argv) == False:
		good_way()
	else:
		nb1 = int(argv[0])
		nb2 = int(argv[1])
		print("Sum:\t\t%d" %(nb1 + nb2))
		print("Difference:\t%d" %(nb1 - nb2))
		print("Product:\t%d" %(nb1*nb2))
		if	nb2 == 0:
			print("Quotient:\tERROR (div by zero)")
			print("Remainder:\tERROR (modulo by zero)")
		else :
			print("Quotient:\t%.1f" %(float(nb1)/float(nb2)))
			print("Remainder:\t%d" %(nb1%nb2))
		
operation(sys.argv[1:])
