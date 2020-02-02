# user inputs 2 number
x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

# first divided by second
result = x / y

# modulo operator used to establish remainder
remainder = x % y

# output presented like so, using format function
print("{} divided by {} is {}, with the remainder {}".format(x, y, result, remainder))
