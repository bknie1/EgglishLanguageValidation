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

operands = ['varint', 'varreal', 'litint', 'litreal']
operators = ['opadd', 'opsub', 'opmult', 'opdiv', 'opidiv', 'opequal']
terms = ['termint', 'termreal']

# varint = re.compile		(r'([i]\w*.)')
# varreal = re.compile	(r'(([r]\w*.)!(varint))')

varint = re.compile		(r'[i]\w*')
varreal = re.compile	(r'(?<!va)(r\w*)') # Don't overwrite varint's by mistake.
litreal = re.compile	(r'\d*[.]\d*')
litint = re.compile		(r'\d')
add = re.compile		(r'\+')
subt = re.compile 		(r'\-')
mult = re.compile		(r'\*')
idiv = re.compile		(r'\/\/')
rdiv = re.compile		(r'[\/]')
equ = re.compile		(r'\=')

termint = re.compile 	(r'(termint|varint|litint)\s(opmult|opidiv)\s(varint|litint)')
termreal = re.compile	(r'(termreal|varreal|litreal)\s(opmult|opidiv)\s(varreal|litreal)')

# Why wouldn't these work? Aren't these better formatted?
# varint = re.compile	(r'([i]\w*)g')
# varreal = re.compile	(r'([r]\w*)g')
# litreal = re.compile	(r'(\d*[.]\d*)g')
# litint = re.compile		(r'(\d)g')
# add = re.compile		(r'(\+)g')
# subt = re.compile		(r'(\-)g')
# mult = re.compile		(r'(\*)g')
# divi = re.compile		(r'(\\)g')
# idiv = re.compile		(r'(\\\\)g')

#FN###############################################################################
def read_file() :
		if len(sys.argv) != 2 : throw_fatal("Missing file.")
		for arg in sys.argv :
			if os.path.isfile(arg) and arg.endswith(".txt") :
				file = open(arg, 'r')
				return file
#--------------------------------------------------------------------------------#
# Phase 1: Replaces operands and operators.
def find_ops(line) :
	# sub(regex/re object, replacement value, string)
	print(line)

	line = re.sub(varint, 'varint', line)
	line = re.sub(varreal, 'varreal', line)
	line = re.sub(litreal, 'litreal', line)
	line = re.sub(litint, 'litint', line)
	line = re.sub(add, 'opadd', line)
	line = re.sub(subt, 'opsub', line)
	line = re.sub(mult, 'opmult', line)

	line = re.sub(idiv, 'opidiv', line)
	line = re.sub(rdiv, 'oprdiv', line)

	line = re.sub(equ, 'opequal', line)

	print(line)
	return line
#--------------------------------------------------------------------------------#
def find_terms(line) :
	line = re.sub(termint, 'termint', line)
	line = re.sub(termreal, 'termreal', line)
	print(line)
	return line
#--------------------------------------------------------------------------------#
def throw_fatal(error) :
	print("Error:", error)
	sys.exit(0)

#MAIN#############################################################################

# Argument Reading and *.txt File Filtering
file = read_file()
for line in file :
	line = find_ops(line)
	line = find_terms(line)