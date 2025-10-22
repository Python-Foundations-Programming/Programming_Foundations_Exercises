# Programming Exercise 9-5

def main():
    # Set up empty dictionary
    counter = {}

    # Get the name of the input file.
    input_name = input('Enter the name of the input file: ')
    text = ''

    # Get input text
    with open(input_name, 'r') as input_file:
        text = input_file.read()
    
    # Split the text into words.
    words = text.split()

    # Add each unique word to dictionary with a counter of 0
    unique_words = set(words)
    for word in unique_words:
        counter[word] = 0

    # For each word in the text increase its counter in the dictionary
    for item in words:
        counter[item] += 1

    # Display results
    print(f'{"Word":15}\t{"Occurrences":15}')
    print('----------------------------------------------')
    while len(counter)>0:

        pair = counter.popitem()
        print(f'{pair[0]:15}{pair[1]:<15}')

# Call the main function.
if __name__ == '__main__':
    main()