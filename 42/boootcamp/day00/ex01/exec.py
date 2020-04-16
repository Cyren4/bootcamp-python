import sys

def	reverse_word(s):
	res = ""
	for c in s:
		res = c + res
	return res

def	reverse(args):
	args.pop(0)
	string = ' '.join(args)
	print(reverse_word(string).swapcase())

reverse(sys.argv)

