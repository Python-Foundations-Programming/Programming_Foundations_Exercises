# The prime_or_composite function accepts an integer
# and displays a message indicating whether the value
# is a prime number or a composite number.

def prime_or_composite(n):
    has_divisor = False
    
    for i in range(2, n):
        if n % i == 0:
            has_divisor = True

    if has_divisor:
        print(f'{n} is composite.')
    else:
        print(f'{n} is prime.')

def main():
    # Get an integer from the user.
    user_num = int(input('Enter an integer greater than 1: '))

    # Create an empty list.
    numbers = []
    
    # Populate the list with numbers.
    for count in range(2, user_num + 1):
        numbers.append(count)

    # Determine whether each element is prime or composite.
    for i in range(len(numbers)):
        prime_or_composite(numbers[i])

if __name__ == '__main__':
    main()