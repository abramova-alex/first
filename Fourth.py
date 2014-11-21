#Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit and print out the converted temperature.


celsius = raw_input('Print temperature in Celsius: ')
celsius = float(celsius)

fahrenheit = celsius * 9 / 5 + 32

print 'In Celsius', celsius, ' converting to', fahrenheit, 'in Fahrenheit\n'

fahrenheit = raw_input('Print temperature in Fahrenheit: ')
fahrenheit = float(fahrenheit)

celsius = (fahrenheit - 32) * 5 / 9

print 'In Fahrenheit', fahrenheit, ' converting to', celsius, 'in Celsius\n'