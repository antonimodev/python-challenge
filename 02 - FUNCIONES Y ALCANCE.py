"""
* EXERCISE:
 * - Create examples of basic functions that represent the different
 *   possibilities of the language:
 *   No parameters or return, with one or multiple parameters, with return...
 * - Check if you can create functions inside functions.
 * - Use some examples of functions already created in the language.
 * - Test the concept of LOCAL and GLOBAL variables.
 * - You must print the result of all examples to the console.
 *   (and keep in mind that each language may have more or less possibilities)
 *
 * EXTRA DIFFICULTY (optional):
 * Create a function that takes two string parameters and returns a number.
 * - The function prints all numbers from 1 to 100. Taking into account that:
 *   - If the number is a multiple of 3, it shows the first parameter string.
 *   - If the number is a multiple of 5, it shows the second parameter string.
 *   - If the number is a multiple of 3 and 5, it shows both concatenated strings.
 *   - The function returns the number of times the number has been printed instead of the texts.
 *
 * Pay special attention to the syntax you should use in each case.
 * Each language follows conventions that you must respect for the code to be understood.
 """

					#############
					# FUNCTIONS #
					#############

# Functions allow us to modularize and automate our code. 
# Python provides built-in functions, but we can also create 
# our own functions that are tailored to our specific project.

def ft_example(): # We use "def_name_(parameters):" to define a new function.
	return None  # Functions can return or not, it depends on what we want to do with it.

def ft_example2():
	return 1

def ft_example3(a):
	if (a == 0):
		return("Hi!")
	return("Bye!")

def ft_recursive(number, is_original_call=True):
    if number == 0 and is_original_call:
        print("0")
        return
    if number < 0:
        number = -number
        print("-")
    if number > 0:
        ft_recursive(number // 10, False)
        print(number % 10)

# Test the recursive_print function

ft_recursive(123)
ft_recursive(0)

# Recreation of function sum()

def ft_sum(*args):
    total = 0
    for num in args:
        total = total + num
    print(f"Sum is: {total}")
    return total

# Test the recursive_print function

ft_sum(12,12,24,2)

# Now we're going to talk about local and global variables
# Global variables can be used throughout the code without any restrictions.
# Global variables must be declared as "global" before modifying them.
# Local variables can be used within their own scope.

variable_global = "Bye"
print(variable_global)

def ft_example4():
      global variable_global
      variable_global = "Hello"

ft_example4()
print(variable_global)

# In the previous test we saw how it works, modify variables throughout the code.

					#############
					#  EXERCISE #
					#############

def ft_exercise(str1: str, str2: str):
    count = 0
    for number in range(1, 101):
        if (number % 5 == 0 and number % 3 == 0):
            count+= 1
            print(f"This is both strings: {str1} and {str2}")
        elif (number % 3 == 0):
            count+= 1
            print(f"This is the first string: {str1}")
        elif (number % 5 == 0):
            count+= 1
            print(f"This is the second string: {str2}")
    return (count)

print(ft_exercise("Dog", "Cat"))

#####################################################################
""" 				#	EXTRA	#
# Create a function that takes a list of integers and a target integer. The function should return a list of tuples.
# Each tuple should contain two integers from the input list that add up to the target integer.
# The same integer from the input list can be used in multiple tuples, but the same tuple should not appear more than once in the output list.
# The order of the tuples and the order of the integers within the tuples does not matter.

# For example, given the input list [1, 2, 3, 4, 5] and the target integer 5, the function should return [(1, 4), (2, 3)].

# If no pairs add up to the target integer, the function should return an empty list.
"""
#####################################################################

def ft_listoftuples(lst: list[int], target: int):
    i = 0
    my_lst = []
    while ((i + 1) < len(lst)):
        j = i + 1
        while (j < len(lst)):
            if (lst[i] + lst[j] == target):
                my_lst.append((lst[i], lst[j]))
            j+= 1
        i+= 1
    return my_lst

print(ft_listoftuples([1,2,4], 4))

"""

Here we got another way to solve it, this time with for loop
 
def ft_listoftuples(lst: list[int], target: int):
    my_lst = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] + lst[j] == target):
                my_lst.append((lst[i], lst[j]))
    return my_lst 

"""