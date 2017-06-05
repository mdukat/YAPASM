"""
MIT License

Copyright (c) 2017 Mateusz Dukat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys

# Reading the code from file
name_of_file = sys.argv[1]
try:
	yapasm = open(name_of_file).read()
except:
	print('File error: '+sys.argv[1])

# Remove the \n
yapasm = yapasm.replace('\n','')

# Split the code to single commands
commands = yapasm.split(';')

# Variables for the output code and actually nothing
brainfuck = ''
nothing = 0

# Converting YAPASM commands into BF commands
for command in commands:
	if command == 'LOOP':
		brainfuck += "["
	elif command == 'EOLOOP':
		brainfuck += "]"
	elif command == 'PRINT':
		brainfuck += "."
	elif command == 'GET':
		brainfuck += ","
	elif command[0:3] == 'ADD':
		brainfuck += '+'*int(command[4::])
	elif command[0:3] == 'DEC':
		brainfuck += '-'*int(command[4::])
	elif command[0:5] == 'MOVEL':
		brainfuck += '<'*int(command[6::])
	elif command[0:5] == 'MOVER':
		brainfuck += '>'*int(command[6::])
	else:
		nothing += 1

# Print the output
print(brainfuck)
