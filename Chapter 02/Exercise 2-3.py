# Programming Exercise 2-3

# Variables to hold the size of the tract and number of acres.
tractSize = 0.0
acres = 0.0

# Constant for the number of square feet in an acre.
SQ_FEET_PER_ACRE = 43560

# Get the square feet in the tract.
tractSize = input('Enter the number of square feet in the tract: ')

# Calculate the acreage.
acres = float(tractSize) / SQ_FEET_PER_ACRE

# Print the number of acres.
print (f'The size of that tract is {acres:.2f} acres.')
