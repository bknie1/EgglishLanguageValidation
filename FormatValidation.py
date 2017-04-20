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

# Integers: 	(^[i|r])([a-zA-Z].*)(\+|\-|\*|\=|//).\d*
# Literal Int:	(\d)[\S]
# Literal Real:	\d*[.]\d*\S
# Integer Var: 	(^[i])([a-zA-Z]\S)
# Real Var: 	(^[r])([a-zA-Z]\S)
# Operators: 	([+|\-|*|/|=]|//)

# Use re.search() to find and replace.

#LIB##############################################################################

import sys
import os
import re

#GLOBAL#DECLARATIONS##############################################################

operands = ['varrint', 'varreal', 'litint', 'litreal']
operators = ['opadd', 'opsub', 'opmult', 'opdiv', 'opidiv', 'opequal']
terms = ['termint', 'termreal']

varreal = re.compile(r'(^[r])([a-zA-Z]\S), s')
varint = re.compile(r'(^[i])([a-zA-Z]\S), s')
litreal = re.compile(r'(\d*[.]\d*\S), s')
litint = re.compile(r'(\d)([\S]), s')

#FN###############################################################################
def read_file() :
		if len(sys.argv) != 2 : throw_fatal("Missing file.")
		for arg in sys.argv :
			if os.path.isfile(arg) and arg.endswith(".txt") :
				return arg
#--------------------------------------------------------------------------------#
def read_line(line) :

	return
#--------------------------------------------------------------------------------#
def throw_fatal(error) :
	print("Error:", error)
	sys.exit(0)

#MAIN#############################################################################

# Argument Reading and *.txt File Filtering
sentence = "iInteger = 3"
#file = read_file()
read_line(sentence)