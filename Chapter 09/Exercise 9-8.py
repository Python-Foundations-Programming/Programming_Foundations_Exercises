# Programming Exercise 9-8

import pickle

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constent for filename
FILENAME = 'emails.dat'

# main function
def main():
    # Get email dictionary.
    emails = load_emails()

    # Initialize variable for user choice.
    choice = 0

    # Process user requests until user quits.
    while choice != QUIT:

        choice = get_user_choice()

        if choice== LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            add(emails)
        elif choice == CHANGE:
            change(emails)
        elif choice == DELETE:
            delete(emails)

    # Pickle the resulting dictionary.
    save_emails(emails)

    print('Information saved.')
    
def load_emails():
    try:
        # Open the file.
        with open(FILENAME, 'rb') as input_file:
            # Unpickle the dictionary.
            email_dict = pickle.load(input_file)

    # Could not open file.
    except IOError:
        # Create empty dictionary.
        email_dict = {}

    # Return the dictionary.
    return email_dict

def get_user_choice():
    # Display menu, get user choice, and validate it
    print()
    print('Menu')
    print('----------------------------------------')
    print('1. Look up an email address')
    print('2. Add a new name and email address')
    print('3. Change an existing email address')
    print('4. Delete a name and email address')
    print('5. Quit the program')
    print()

    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice>QUIT:
        choice = int(input('The choice you entered is invalid. '
                           'Please enter a valid choice: '))

    # Return user's choice.
    return choice

def look_up(emails):
    # Get a name to look up.
    name = input('Enter a name: ')

    # Look name up in the dictionary.
    if name in emails:
        print(f' Name: {name}')
        print(f'Email: {emails[name]}')
    else:
        print('The specified name was not found.')

def add(emails):
    # Get name and email address.
    name = input('Enter name: ')
    address = input('Enter email address: ')

    # Add new address if name does not exist.
    # Otherwise, notify user that name exists.
    if name not in emails:
        emails[name] = address
        print('Name and address have been added.')
    else:
        print('That name already exists.')

def change(emails):
    # Get name to update information.
    name = input('Enter name: ')

    # Change address if name exists.
    # Otherwise, notify user that name does not exist.
    if name in emails:
        address = input('Enter the new address: ')
        emails[name] = address
        print('Information updated.')
    else: # name not found
        print('The specified name was not found.')

def delete(emails):
    # Get name to delete.
    name = input('Enter name: ')

    if name in emails:

        del emails[name]
        print('Information deleted.')

    else: # name not found
        print('The specified name was not found.')

# Function pickles the specified dictionary
# and saves it to the emails file.
def save_emails(emails):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(emails, output_file)

    # Close the file.
    output_file.close()

# Call the main function.
if __name__ == '__main__':
    main()