# Programming Exercise 8-8

def main():
    # Get the string as input from the user.
    user_string = input('Enter a string for the program '
                        'to capitalize sentences: ')

    # Call the capitalize function, storing the result.
    result = capitalize(user_string)

    # Display the result.
    print(result)

# The capitalize method receives a string and returns
# the same string with the first letters of all
# sentences capitalized
def capitalize(string):
    # Initialize variables
    result = ''
    new_sentence = True
    result_word = ''

    # Obtain all the words in the string.
    words = string.split()

    # For each word in the string:
    for item in words:
       # The word is the beginning of a new sentence.
        if new_sentence:
            # Create new word where first letter is capitalized.
            result_word = item[0].upper() + item[1:]
        else:
            # Do nothing.
            result_word = item

        # Add resulting word to the string.
        result = result + result_word + ' '

        # If the last character in the word indicates 
        # the end of a sentence, set flag to ensure
        # that next word will be treated as new sentence.
        if item[-1] == '.' or item[-1] == '?' or item[-1] == '!':
            new_sentence = True
        else:
            new_sentence = False

    # Return the result.
    return result

# Call the main function.
if __name__ == '__main__':
    main()