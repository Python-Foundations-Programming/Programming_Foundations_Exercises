# Programming Exercise 5-2

# Global constants for the state and county tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# maindef
def main():
    # Local variables
    purchase = 0.0
    stateTax = 0.0
    countyTax = 0.0

    # Get the amount of the purchase
    purchase = float(input('Enter the purchase amount: '))
    
    # Calculate the state tax
    stateTax = purchase * STATE_TAX_RATE

    # Calculate the county tax
    countyTax = purchase * COUNTY_TAX_RATE

    # Print information about the sale
    showSale(purchase, stateTax, countyTax)

# The showSale function accepts purchase, stateTax,
# countyTax as arguments and prints the equivalent
# total sale information.
def showSale (purchase, stateTax, countyTax):
    #local variables
    totalTax = 0.0
    totalSale = 0.0
    totalTax = stateTax + countyTax
    totalSale = purchase + totalTax
    
    print (f'Purchase amount: {purchase:,.2f}')
    print (f'State tax: {stateTax:,.2f}')
    print (f'County tax: {countyTax:,.2f}')
    print (f'Total tax: {totalTax:,.2f}')
    print (f'Sale total: {totalSale:,.2f}')

# Call the main function.
main()
