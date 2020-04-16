import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----'} 

def	check(av):
	for i in av:
		if not i.isalnum() or i.isspace():
			return False
	return True

def	encodage(av):
	if not check(av) :
		print "ERROR"
	else:
		string = ' '.join(av)
		string = string.upper()
		translate = ''
		for i in string:
			if i.isspace():
				translate += " / "
			else:
				translate += MORSE_CODE_DICT[i] + ' '
		print translate[:len(translate) - 1]

if len(sys.argv) > 1:
	encodage(sys.argv[1:])
