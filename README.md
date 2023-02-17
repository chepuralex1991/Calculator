CALCULATOR
This is a simple command-line calculator program that can perform basic arithmetic operations on numbers in different number bases. The calculator supports the following bases: binary (base-2), decimal (base-10), hexadecimal (base-16), base-36, and base-62.

PROJECT STRUCTURE
The project is structured into three Python files:

main.py: This is the main program file that the user runs to perform calculations. It imports the from_base and to_base functions from the calculator.converter module to convert input numbers. It also imports the evaluate function from the calculator.evaluation module to perform arithmetic operations on the converted numbers.

evaluation.py: This module defines the evaluate function, which takes two  numbers and an operation choice as input and returns the result of the operation. The module also defines four separate functions (add, subtract, multiply, divide) for each arithmetic operation.

converter.py: This module defines the from_base and to_base functions, which convert input numbers from their specified base to decimal and back to the specified base, respectively. 