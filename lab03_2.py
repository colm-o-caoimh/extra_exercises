# initial attempt without checking the answer

x = float(input("Enter a number: "))
y = float(input("Now, enter another number: "))

result = y - x

print("The difference is " + str(result))

# second attempt using the format function
x = int(input("Enter a number: "))
y = int(input("Now, please enter another number: "))

result = y - x

print("{} minus {} is {}".format(y, x, result))

