# Name: 		Assignment 4 : Format Validation
# Description : Validates format of a pretend language via input file.
# Author:		Brandon Knieriem
# Notes:
# 	- Integer variable names begin with i followed by letters.
# 		- Replace integer names with 'varint'
# 	- Real variable names begin with r followed by letters.
# 		- Replace real names with 'varreal'
# 	- Literal integer: Non-zero digits preceded by + or -.
# 		- Replace with litint.
# 	- Literal real: Numbers, then '.', then numbers.
# 		- Replace with litreal.
# 	- Print out intermediate versions of the expression string after replacements
# 		for each type of operand have occurred.
# 	- Operands: =, +, - , *, /, //.
# 		- Replace with opequal, opadd, opsub, opmult, oprdiv, opidiv.
# 	- Error if revised expression features anything other than these operator or
# 		operand replaceents.

# (^[i|r])([a-zA-Z].*)(\+|\-|\*|\=|//).\d*

#LIB##############################################################################

import sys
import os
import re

#GLOBAL#DECLARATIONS##############################################################



#FN###############################################################################
def read_file() :
		if len(sys.argv) != 2 : throw_fatal("Missing file.")
		for arg in sys.argv :
			if os.path.isfile(arg) and arg.endswith(".txt") :
				return arg
#--------------------------------------------------------------------------------#
def read_line() :
	return
#--------------------------------------------------------------------------------#
def throw_fatal(error) :
	print("Error:", error)
	sys.exit(0)

#MAIN#############################################################################

# Argument Reading and *.txt File Filtering

#file = read_file()

sentence = "iInteger = 3"

print(re.split(r'\s*', sentence))
print(re.split(r'\s*', "Testing this regex."))