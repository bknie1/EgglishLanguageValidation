# Egglish Programming Language Validator

Validates the format of a made-up programming language using a pre-determined input file.

## Rules
- Integer variable names begin with i followed by letters.
- Replace integer names with 'varint'
- Real variable names begin with r followed by letters.
- Replace real names with 'varreal'
- Literal integer: Non-zero digits preceded by + or -.
- Replace with litint.
- Literal real: Numbers, then '.', then numbers.
- Replace with litreal.
- Print out intermediate versions of the expression string after replacements or each type of operand have occurred.
- Operands: =, +, - , *, /, //.
- Replace with opequal, opadd, opsub, opmult, oprdiv, opidiv.
- Error if revised expression features anything other than these operator or operand replaceents.
