import string
import sys

def	text_analyzer(s = None):

	up = 0
	low = 0
	punc = 0
	space = 0
	if not s :
		s = input("What is the text to analyse?\n>>")
	for i in s:
		if (i.islower()):
			low +=1	
		elif (i.isupper()):
			up +=1	
		elif (i.isspace()):
			space +=1	
		if (i in string.punctuation):
			punc +=1	
	print("The text countains %d characters :" % (len(s)))
	print("- %d upper letters" % (up))
	print("- %d lower letters" %(low))
	print("- %d punctuation marks" %(punc))
	print("- %d spaces" %(space))

