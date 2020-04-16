import sys

def	check_param(s):
	if (s[0] == '-' or s[0] == '+'):
		s = s[1:]
	return s.isdigit()

def	check_nb(args):

	if len(args) == 0:
		exit()
	if (len (args) != 1 or check_param(args[0]) == False):
		print("ERROR")
	else :
		nb = int(args[0])
		if (nb == 0):
			print("I'm Zero.")
		else:
			print("I'm Even." if nb % 2 == 0 else "I'm Odd.")

check_nb(sys.argv[1:])
