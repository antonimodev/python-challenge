"""
 * EXERCISE:
 * - Create examples using all types of operators in your language:
 *   Arithmetic, logical, comparison, assignment, identity, membership, bitwise...
 *   (Keep in mind that each language may have different operators)
 * - Using operations with operators of your choice, create examples
 *   that represent all types of control structures in your language:
 *   Conditionals, loops, exceptions...
 * - You must print the result of all examples to the console.
 *
 * EXTRA CHALLENGE (optional):
 * Create a program that prints to the console all numbers between 10 and 55 (inclusive)
 * that are even and not equal to 16 or multiples of 3.
 *
 * By carefully reviewing the possibilities, you may discover something new.
 """
					########################
					# ARITHMETIC OPERATORS #
					########################

# Addition operator
addition = 2 + 2
print(f"Addition operator: 2 + 2 = {addition}")

# Subtraction operator
subtraction = 2 - 2
print(f"Subtraction operator: 2 - 2 = {subtraction}")

# Multiplication operator
multiplication = 2 * 2
print(f"Multiplication operator: 2 * 2 = {multiplication}")

# Division operator
division = 2 / 2
print(f"Division operator: 2 / 2 = {division}")

# Integer division operator
integer_division = 2 // 2
print(f"Integer division operator: 2 // 2 = {integer_division}")

# Module operator
module = 2 % 2
print(f"module operator: 2 % 2 = {module}")

# Exponentiation operator
exponentiation = 2 ** 2
print(f"Exponentiation operator: 2 ** 2 = {exponentiation}")

					#####################
					# LOGICAL OPERATORS #
					#####################

# '&&' operator // 'and'
# Returns True if both operands are true
print(f"'and' operator: True and False = {True and False}")

# '||' operator // 'or'
# Returns True if either operand is true
print(f"'or' operator: True or False = {True or False}")

# 'not' operator
# Returns True if the operand is false (complement)
print(f"'not' operator: not True = {not True}")

					########################
					# COMPARISON OPERATORS #
					########################

# '==' operator // Equal to
# Returns True if both operands are equal
print(f"'==' operator: 10 == 20 = {10 == 20}")

# '!=' operator // Not equal to
# Returns True if both operands are different
print(f"'!=' operator: 10 != 20 = {10 != 20}")

# '<' operator // Less than
# Returns True if the left operand is less than the right operand
print(f"'<' operator: 10 < 20 = {10 < 20}")

# '<=' operator // Less than or equal to
# Returns True if the left operand is less than or equal to the right operand
print(f"'<=' operator: 10 <= 20 = {10 <= 20}")

# '>' operator // Greater than
# Returns True if the left operand is greater than the right operand
print(f"'>' operator: 10 > 20 = {10 > 20}")

# '>=' operator // Greater than or equal to
# Returns True if the left operand is greater than or equal to the right operand
print(f"'>=' operator: 10 >= 20 = {10 >= 20}")

					########################
					# ASSIGNMENT OPERATORS #
					########################

a = 10

# '=' operator // Assignment
# Assigns the value of the right operand to the left operand
print(f"'=' operator: a = 10 => a = {a}")

# '+=' operator // Addition and assignment
# Adds the right operand to the left operand and assigns the result to the left operand
a += 5
print(f"'+=' operator: a += 5 => a = {a}")

# '-=' operator // Subtraction and assignment
# Subtracts the right operand from the left operand and assigns the result to the left operand
a -= 2
print(f"'-=' operator: a -= 2 => a = {a}")

# '*=' operator // Multiplication and assignment
# Multiplies the right operand by the left operand and assigns the result to the left operand
a *= 3
print(f"'*=' operator: a *= 3 => a = {a}")

# '/=' operator // Division and assignment
# Divides the left operand by the right operand and assigns the result to the left operand
a /= 4
print(f"'/=' operator: a /= 4 => a = {a}")

# '%=' operator // Module and assignment
# Takes the module of the left operand with the right operand and assigns the result to the left operand
a %= 3
print(f"'%=' operator: a %= 3 => a = {a}")

# '**=' operator // Exponentiation and assignment
# Raises the left operand to the power of the right operand and assigns the result to the left operand
a **= 2
print(f"'**=' operator: a **= 2 => a = {a}")

# '//=' operator // Integer division and assignment
# Divides the left operand by the right operand, rounds the result down to the nearest integer, and assigns the result to the left operand
a //= 2
print(f"'//=' operator: a //= 2 => a = {a}")

					######################
					# IDENTITY OPERATORS #
					######################

# 'is' operator
# Returns True if both variables are the same object
x = 5
y = 5
print(f"'is' operator: x is y = {x is y}")  # True

# 'is not' operator
# Returns True if both variables are not the same object
a = [1, 2, 3]
b = [1, 2, 3]
print(f"'is not' operator: a is not b = {a is not b}")  # True

# Note: 'is' and 'is not' are different from '==' and '!='
# 'is' and 'is not' compare if two variables point to the same object in memory
# '==' and '!=' compare the values of the objects

					########################
					# MEMBERSHIP OPERATORS #
					########################

# List of numbers
numbers = [1, 2, 3, 4, 5]

# in operator
print(f"3 is in numbers: {3 in numbers}")  # Returns True because 3 is in the list

# not in operator
print(f"6 is not in numbers: {6 not in numbers}")  # Returns True because 6 is not in the list

					#####################
					# BITWISE OPERATORS #
					#####################

# Bitwise AND operator
# Performs a bitwise AND operation on the binary representations of two numbers
print(f"Bitwise AND operator: 5 & 3 = {5 & 3}")  # Returns 1

# Bitwise OR operator
# Performs a bitwise OR operation on the binary representations of two numbers
print(f"Bitwise OR operator: 5 | 3 = {5 | 3}")  # Returns 7

# Bitwise XOR operator
# Performs a bitwise XOR operation on the binary representations of two numbers
print(f"Bitwise XOR operator: 5 ^ 3 = {5 ^ 3}")  # Returns 6

# Bitwise NOT operator
# Performs a bitwise NOT operation on the binary representation of a number
print(f"Bitwise NOT operator: ~5 = {~5}")  # Returns -6

# Left shift operator
# Shifts the binary representation of a number to the left by a specified number of positions
print(f"Left shift operator: 5 << 1 = {5 << 1}")  # Returns 10

# Right shift operator
# Shifts the binary representation of a number to the right by a specified number of positions
print(f"Right shift operator: 5 >> 1 = {5 >> 1}")  # Returns 2

					####################
					# WALRUS OPERATOR #
					####################

# Walrus operator (:=)
# Assigns a value to a variable as part of an expression
# Let's say we have a list of numbers
numbers = list(range(1, 10))

# We want to check if the length of the list is greater than 5
# and print the length if it is. Without the walrus operator, we might do:

length = len(numbers)
if length > 5:
    print(f"The list has more than 5 elements, it has {length} elements.")

# With the walrus operator, we can do this in a more concise way:

if (length := len(numbers)) > 5:
    print(f"The list has more than 5 elements, it has {length} elements.")

# We assign numbers lenght to a variable lenght then we check if it is greater than 5.
# It's more important focus on readability than efficiency, so Walrus may not
# the best option

#########################################################################################
""" 				#	EXERCISES	#
# Create a program that prints to the console all numbers between (X) and (Y) (inclusive)
that are even and not equal to (Z) or multiples of (A).
"""
#########################################################################################

# FROM 10 TO 55. OMIT 16 AND MULTIPLES OF 3
for i in range(10, 56):
	if (i % 2 == 0) and (i != 16) and (i % 3 != 0):
		print(i)

# FROM 20 TO 100. OMIT MULTIPLES OF 5
for i in range(20, 101):
	if (i % 5 != 0):
		print(i)

# FROM 1 TO 1000. MULTIPLES OF 7. OMIT MULTIPLES OF 5
for i in range(1, 1001):
	if (i % 7 == 0) and (i % 5 != 0):
		print(i)

# FROM 50 TO 150. MULTIPLES OF 3 AND 5. OMIT MULTIPLES OF 10
for i in range(50, 151):
	if (i % 3 == 0) and (i % 5 == 0) and (i % 10 != 0):
		print(i)

# FROM 200 TO 300. MULTIPLES OF 4. OMIT MULTIPLES OF 6 AND 8
for i in range(200, 301):
	if (i % 4 == 0) and (i % 6 != 0) and (i % 8 != 0):
		print(i)

# FROM 100 TO 200. MULTIPLES OF 5. OMIT 150 AND MULTIPLES OF 10
for i in range(100, 201):
	if (i % 5 == 0) and (i != 150) and (i % 10 != 0):
		print(i)

#####################################################################
""" 				#	EXTRA	#
# Create a program that prints all prime numbers between 1 and 1000
that are also multiples of 7 but not multiples of 5.
"""
#####################################################################


def is_prime(number):
	"""
	Check if a number is prime.
	
	ARG TYPE: INT.
	
	RETURN VALUES: True or False.
	"""
	if number <= 1:
		return False
	for i in range(2, number):
		if number % i == 0:
			return False
	return True


for i in range(1, 1001):
    if is_prime(i) and (i % 7 == 0) and (i % 5 != 0):
        print(i)
