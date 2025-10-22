# Programming Exercise 4-6

# Declare a variable to hold the temperature
# in degrees Fahrenheit.
fahrenheit = 0.0

# Calculate and print value for each temperature.
print ('Celsius\t\tFahrenheit')
print ('------------------------------------------')

for celsiusDegree in range(21):
    fahrenheit = ((9 * celsiusDegree) / 5) + 32
    print (celsiusDegree, '\t\t', fahrenheit)
