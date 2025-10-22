# Programming Exercise 7-1

def main():
    # Variables
    total_sales = 0.0

    # Initialize lists
    daily_sales = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    days_of_week = ['Sunday', 'Monday', 'Tuesday',
                    'Wednesday', 'Thursday', 'Friday',
                    'Saturday']

    for i in range(7):
        daily_sales[i] = float(input('Enter the sales for '
                                     + days_of_week[i] + ': '))

    for number in daily_sales:
        total_sales += number

    # Display total sales
    print (f'Total sales for the week: ${total_sales:,.2f}')

# Call the main function.
if __name__ == '__main__':
    main()