# Programming Exercise 4-11

# Inititalize number to zero.
number = 0 

# Get a valid number from the user.
while number <= 0:
    number = int(input('Enter a nonnegative integer: '))

# Initialize the accumulator variable.
factoral = 1

# Calculate the factoral of the number.
for factor in range(1, number + 1):
    factoral *= factor

# Display the factoral of the number.
print(f'The factoral of {number} is {factoral:,d}')
