# Colm O'Caoimh
# Create program which prints out queue of random numbers, then removes the first
# element in the queue as it prints out the updated list

from random import seed
from random import randint

# initialise empty list
num_list = []

# generate list of 10 random numbers between 1 and 100
for x in range(10):
    value = randint(0, 100)
    num_list.append(value)
print("queue is:", num_list)

# remove element at index 0 on each loop and print updated queue
for x in range(10):
    y = num_list.pop(0)
    print("current Number is", y, "and the queue is", num_list)

print("The queue is now empty")