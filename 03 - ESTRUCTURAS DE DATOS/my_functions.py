# My library

def add_contact(contact_list: dict):
	"""
	Prompts the user for a phone number and a contact name,
	then adds these data to the provided contact dictionary.

	Parameters:
	contact_list (dict): The contact dictionary to which the new contact will be added.
	"""
	while True:
		phone_number = input("Enter the phone number\n")
		number_len = len(phone_number)
		if number_len != 11 or not phone_number.isdigit():
			print("The format should have a prefix, something like this: 34654849943")
		else:
			break
	phone_contact = input("Enter the name of your contact\n")
	while True:
		if not phone_contact.strip():
			print("Name cannot be empty")
		else:
			break
	contact_list[phone_contact] = phone_number 
	print("Contact added successfully\n")

def remove_contact(contact_list: dict):
	"""
	Prompts the user for a contact name and, if it exists in the contact dictionary,
	removes it.

	Parameters:
	contact_list (dict): The contact dictionary from which the contact will be removed.
	"""
	remove_contact = input("Which contact do you want to remove?\n")
	if remove_contact not in contact_list:
		print("The contact does not exist.\n")
	while remove_contact in contact_list:
		confirm = input(f"Sure about remove {remove_contact}? Y\\N\n")
		if confirm == 'y' or confirm == 'Y':
			contact_list.pop(remove_contact)
			print("Contact removed successfully\n")
		elif confirm == 'n' or confirm == 'N':
			return
		else:
			print("You should write Y\\N\n")

def show_contact_list(contact_list: dict):
	"""
	Prints all the contacts in the provided contact dictionary.

	Parameters:
	contact_list (dict): The contact dictionary to be printed.
	"""
	print("This is your contact list:\n")
	for key, value in contact_list.items():
		print(f"""
		Name: {key}
		Phone number: {value}\n""")
