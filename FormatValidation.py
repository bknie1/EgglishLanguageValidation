# Name: 		Assignment 4 : Format Validation
# Description : Validates format of a pretend language via input file.
# Author:		Brandon Knieriem
# Notes:
# 	- Integer variable names begin with i followed by letters.
# 		- Replace integer names with 'varint'
# 	- Real variable names begin with r followed by letters.
# 		- Replace real names with 'varreal'
# 	- Literal integer: Non-zero digits preceded by + or -.
# 	- Literal real: Numbers, then '.', then numbers.

#LIB##############################################################################

import sys
import os

#GLOBAL#DECLARATIONS##############################################################



#FN###############################################################################
def read_file() :
	try :
		for arg in sys.argv :
			if os.path.isfile(arg) and arg.endswith(".txt") :
				return arg
	except : throw_fatal("No file.")
#--------------------------------------------------------------------------------#
def throw_fatal(error) :
	print("Error:", error)
	sys.exit(0)

#MAIN#############################################################################

# Argument Reading and *.txt File Filtering

file = read_file()