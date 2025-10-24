# Programming Exercise 6-4

def main():
    # Declare variables
    line = ''
    counter = 0

    # Open names.txt file for reading
    with open('names.txt', 'r') as infile:
        # Priming read
        line = infile.readline()
        
        # Read in until no more data
        while line != '':
            counter += 1
            line = infile.readline()
    
    # Display the number of names in the file
    print (f'{counter} names were read.')

# Call the main function.
if __name__ == '__main__':
    main()