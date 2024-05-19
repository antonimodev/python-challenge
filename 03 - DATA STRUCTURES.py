""" 
 * EXERCISE:
 * - Show examples of creating all the default supported structures in your language.
 * - Use insertion, deletion, update, and sorting operations.
 *
 * EXTRA DIFFICULTY (optional):
 * Create a contact agenda via terminal.
 * - You must implement search, insertion, update, and deletion functionalities for contacts.
 * - Each contact must have a name and a phone number.
 * - The program first asks what operation you want to perform, and then
 *   the necessary data to carry it out.
 * - The program cannot allow the introduction of non-numeric phone numbers and with more than 11 digits.
 *   (or the number of digits you want)
 * - An operation to end the program should also be proposed.
 """
 
					#############
					#   LISTS   #
					#############
     
# Lists are grouped elements in an order that can vary either by adding/removing
# Or modifying elements of that list.
# Lists use the syntax []

my_list = [1, 2, 3, 4, 5]

# Test of element insertion

my_list.append(5)  # Adds an element at the end of the list.
my_list.insert(0, 2)  # Adds the element 2 at position 0.

# Test of element indexing

print(my_list.index(3))  # Returns the index of the first element with the specified value.
print(my_list.count(3))  # Returns the number of times the element appears in the list.
my_list.reverse()  # Reverses the order of the elements in the list.
print(my_list)

# Test of element removal

my_list = [1, 2, 3, 4]
my_list.pop(0)  # Removes the element at position 0.

# Test of element sorting

my_list = [1, 5, 3, 4, 2]
my_list.sort()  # Sorts the list.
print(my_list)  # Prints the sorted list.

					#############
					#   TUPLES  #
					#############
     
# Tuples are immutable lists, they cannot be modified.
# Tuples use the syntax ()

my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in a tuple
print(my_tuple[0])  # Prints the first element of the tuple

# Slicing a tuple
print(my_tuple[1:3])  # Prints elements from index 1 to 2

# Finding the length of a tuple
print(len(my_tuple))  # Prints the number of elements in the tuple

# Counting the occurrence of a specific value in a tuple
print(my_tuple.count(2))  # Prints the number of times 2 appears in the tuple

# Finding the first occurrence of a specific value in a tuple
print(my_tuple.index(3))  # Prints the index of the first occurrence of 3 in the tuple

# Checking if an element exists in a tuple
print(3 in my_tuple)  # Prints True if 3 is in the tuple, False otherwise

					################
					# DICTIONARIES #
					################
     
# Dictionaries are unordered elements but have a relationship between pairs.
# Dictionaries use the syntax {}

my_dict = {"name": "Antonio", "year": "1998"}

# Test of operations with dictionary elements

my_dict = {"name": "Samara", "year": "1997"}  # Dictionary definition
print(my_dict.get("name"))  # Returns the value of the key name.
print(my_dict.keys())  # Returns a view of the keys.
print(my_dict.values())  # Returns a view of the values.
print(my_dict.items())  # Returns a view of the key-value pairs of the dict.
my_dict.pop("name")  # Removes the key-value pair.

my_other_dict = {"example": "hello"}
my_dict.update(my_other_dict)  # Updates a dictionary with the information from the other.

					#############
					#   SETS    #
					#############
     
# Sets are a list of unique elements. Duplicates are not allowed.
# Sets use the syntax {} like in dictionaries, only they are not associated
# In pairs.

my_set = {1, 2, 3, 4, 5}

# Test with sets

# Creation of a second set to demonstrate operations between sets
my_other_set = {4, 5, 6, 7, 8}

# Union of sets: returns a set containing all elements from both sets, without duplicates.
union_set = my_set.union(my_other_set)
print("Union:", union_set)

# Intersection of sets: returns a set containing the elements that exist in both sets.
intersection_set = my_set.intersection(my_other_set)
print("Intersection:", intersection_set)

# Difference of sets: returns a set containing the elements that exist in the first set but not in the second.
difference_set = my_set.difference(my_other_set)
print("Difference:", difference_set)

# Symmetric difference of sets: returns a set containing the elements that exist only in one of the sets, but not in both.
symmetric_difference_set = my_set.symmetric_difference(my_other_set)
print("Symmetric Difference:", symmetric_difference_set)

# Test of operations with sets

my_set.add(6)  # Adds an element to the set.
my_set.remove(1)  # Removes an element from the set.
print(my_set)  # Prints the set.


					#############
					#  EXERCISE #
					#############
     
while True:
    user_choice = input("""
	¡Hola, bienvenid@ a tu agenda telefónica!
	¿Qué quieres hacer?
	1.- Agregar contacto
	2.- Eliminar contacto
	3.- Salir del programa
	""")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice in [1, 2, 3]:
            break
        else:
            print("Por favor, introduce 1, 2 o 3.")
    else:
        print("Por favor introduzca un número")