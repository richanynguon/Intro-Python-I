"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print('x is %d, y is %7.5f, z is "%s"' %(10, 2.24552, "I like turtles!"))

# Use the 'format' string method to print the same thing
print('x is {0}, y is {1}, z is "{2}"'.format(x, y, z))

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y}, z is "{z}"')

# Strings (%s) Numbers (%d)   Float (6 number of total characters, 2 decimal places == %6.2f)
