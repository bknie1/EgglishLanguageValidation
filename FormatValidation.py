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
# 	- I understand why regex is valuable but this gave me a headache. Super burned out.
#LIB##############################################################################

import sys
import os
import re

#GLOBAL#DECLARATIONS##############################################################

terms = ['varint', 'varreal', 'litint', 'litreal', 'opadd', 'opsub', 'opmult',
'oprdiv', 'opidiv', 'opequal', 'termint', 'termreal', 'subint', 'subreal', 'statement']

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

termint = re.compile(r'(termint|varint|litint)\s(opmult|opidiv)\s(varint|litint)')
termreal = re.compile(r'(termreal|varreal|litreal)\s(opmult|opidiv)\s(varreal|litreal)')

subint = re.compile(r'(subint|varint|litint|termint)\s(opadd|opsub)(varint|litint|termint)')
subreal = re.compile(r'(subreal|varreal|litreal|termreal)\s(opadd|opsub)(varreal|litreal|termreal)')

statement = re.compile(r'((varint)\s(opequal)\s(litint|varint|termint|subint))|((varreal)\s(opequal)\s(litreal|varreal|termreal|subreal))')

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
	print(line.strip())

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

	print(line.strip())
	return line
#--------------------------------------------------------------------------------#
def find_terms(op_line) :
	op_line = re.sub(termint, 'termint', op_line)
	op_line = re.sub(termreal, 'termreal', op_line)
	print(op_line.strip())
	return op_line
#--------------------------------------------------------------------------------#
def find_sub(term_line) :
	term_line = re.sub(subint, 'subint', term_line)
	term_line = re.sub(subreal, 'subreal', term_line)
	print(term_line.strip())
	return term_line
#--------------------------------------------------------------------------------#
def find_statement(sub_line) :
	sub_line = re.sub(statement, 'statement', sub_line)
	print(sub_line.strip())
	return sub_line
#--------------------------------------------------------------------------------#
def error_checking(sub_line) :
	flag = 1
	if len(sub_line) == 0 :
		if sub_line != 'statement': throw_fatal("Invalid syntax.")
	else :
		for word in line :
			for ops in terms :
				if word is ops:
					flag == 0
		if flag == 0 :
			throw_fatal("Invalid syntax.")
#--------------------------------------------------------------------------------#
def throw_fatal(error) :
	print("Error:", error)
	sys.exit(0)
#MAIN#############################################################################

# Argument Reading and *.txt File Filtering
file = read_file()
for line in file :
	print("===========================================================================")
	line = find_ops(line)
	line = find_terms(line)
	line = find_sub(line)
	line = find_statement(line)
	line = line.split()
	error_checking(line)
	print("===========================================================================")