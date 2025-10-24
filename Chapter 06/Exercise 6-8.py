# Programming Exercise 6-8

def main():
    # Local variables
    counter = 0
    total = 0
    number = 0    

    # Open input file
    with open('random_numbers.txt', 'r') as inputFile:
        # Read numbers from the file while keeping count 
        # and a running total
        for line in inputFile:
            number = int(line)
            total += number
            counter += 1

    print(f'Total: {total:,}')
    print(f'{counter} numbers were read from the file.')

# Call the main function.
if __name__ == '__main__':
    main()