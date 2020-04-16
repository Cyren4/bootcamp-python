import sys
import string

def	check_param(av):
	if len(av) != 2:
		return False
	else :
		if not av[1].isdigit() or av[0].isdigit():
			return False
	return True

def	filter(argv):
	if not check_param(argv):
		print ("ERROR")
	else :
		argv[0] = argv[0].translate(str.maketrans('', '', string.punctuation))
		print ([x for x in argv[0].split() if len(x) > int(argv[1]) and not x in string.punctuation])
		
filter(sys.argv[1:])
