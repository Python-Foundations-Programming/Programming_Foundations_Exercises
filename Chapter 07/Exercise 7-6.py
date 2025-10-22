# Programming Exercise 7-6

def main():
    # Declare local variables
    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display the number.
    print('Number:', number)

    # Display the list of numbers.
    print('List of numbers:')
    print(f'{number_list}')
    
    # Display the list of numbers that are larger
    # than the number.
    print(f'List of numbers that are larger than {number}:')
    
    # Call the display_larger_than_n_list function,
    # passing a number and number list as arguments.
    display_larger_than_n_list(number, number_list)

# The display_larger_than_n_list function accepts two arguments:
# a list, and a number. The function displays all of the numbers
# in the list that are greater than the number.
def display_larger_than_n_list(n, n_list):
    # Declare an empty list.
    larger_than_n_list = []

    # Loop through the values in the list.
    for value in n_list:
        
        # Determine if a value is greater than n.
        if value > n:
            
            # If so, append the value to the list.
            larger_than_n_list.append(value)

    # Display the list.
    print(larger_than_n_list)
        
# Call the main function.
if __name__ == '__main__':
    main()