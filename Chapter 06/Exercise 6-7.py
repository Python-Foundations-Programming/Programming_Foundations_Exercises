# Programming Exercise 6-7
import os
import random


def main():
    try:
        # Ask the user for the filename
        filename = input(
            "Enter the name of the file to which results should be written: ").strip()
        if not filename:
            raise ValueError("No filename was entered!")

        # Ask for the number of random numbers to generate
        try:
            number_of_randoms = int(
                input("Enter the number of random numbers to be written to the file: "))
        except ValueError:
            raise ValueError(
                "Invalid input! Please enter an integer greater than zero.")

        if number_of_randoms <= 0:
            raise ValueError(
                "Number of random numbers must be greater than zero.")

        # Create full file path inside the "Chapter 06" folder
        filename = os.path.join("Chapter 06", filename)

        # Use a context manager to safely write random numbers
        with open(filename, 'w') as outputFile:
            for _ in range(number_of_randoms):
                random_number = random.randint(1, 500)
                outputFile.write(str(random_number) + '\n')

        # Confirmation message
        print(
            f"Successfully wrote {number_of_randoms} random numbers to '{filename}'.")

    except ValueError as e:
        print(f"Error: {e}")
    except OSError as e:
        print(f"File error: {e}")


# Call the main function
if __name__ == '__main__':
    main()
