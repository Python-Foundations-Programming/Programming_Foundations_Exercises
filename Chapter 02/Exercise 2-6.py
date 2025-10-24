# Programming Exercise 2-6

# Variable declarations
purchase = 0.0
stateTax = 0.0
countyTax = 0.0
totalTax = 0.0
totalSale = 0.0

# Constants for the state and county tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Get the amount of the purchase.
purchase = float(input('Enter the amount of the purchase: '))

# Calculate the state sales tax.
stateTax = purchase * STATE_TAX_RATE

# Calculate the county sales tax.
countyTax = purchase * COUNTY_TAX_RATE

# Calculate the total tax.
totalTax = stateTax + countyTax

# Calculate the total of the sale.
totalSale = purchase + totalTax

# Print information about the sale.
print (f'Purchase Amount: {purchase:,.2f}')
print (f'State Tax: {stateTax:,.2f}')
print (f'County Tax: {countyTax:,.2f}')
print (f'Total Tax: {totalTax:,.2f}')
print (f'Sale Total: {totalSale:,.2f}')
