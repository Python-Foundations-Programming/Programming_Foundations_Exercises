# Programming Exercise 3-7

# Global variables
RED = 'red'
BLUE = 'blue'
YELLOW = 'yellow'

# Get first color from the user.
color1 = input('Enter the first primary color in lower case letters: ')

# Get second color from the user.
color2 = input('Enter the second primary color in lower case letters: ')

# Check validity of first color.
if color1 != RED and color1 != BLUE and color1 != YELLOW:
    print('Error: The first color you entered is invalid.')

# Check validity of second color.
elif color2 != RED and color2 != BLUE and color2 != YELLOW:
    print('Error: The second color you entered is invalid.')

# Check if the two colors are the same.
elif color1 == color2:
    print('Error: The two colors you entered are the same.')

# Display the secondary color resulting from mixing the two colors.
else:
    # Determine secondary color if the first color is red.
    if color1 == RED:
        if color2 == BLUE:
            print('purple')
        else: # Color 2 must be yellow
            print('orange')

    # Determine secondary color if first color is blue.
    elif color1 == BLUE:
        if color2 == RED:
            print('purple')
        else: # Color 2 must be yellow.
            print('green')

    else: # First color must be yellow.
        if color2 == RED:
            print('orange')
        else: # Color 2 must be blue.
            print('green')
