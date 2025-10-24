# Programming Exercise 6-1

def main():
    try:
        # Use a context manager to open and read the file
        with open('Chapter 06/numbers.txt', 'r') as infile:
            contents = infile.read()
            tokens = contents.split()

    except FileNotFoundError as e:
        print(f"Error: {e}")

    else:
        # Print contents after the file is closed
        if not contents:
            print("The file does not contain any data!")
        else:
            print(contents)
            print("Count:", len(tokens))


# Call the main function.
if __name__ == '__main__':
    main()
