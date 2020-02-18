from random import seed
from random import randint


num_list = []

for x in range(10):
    value = randint(0, 100)
    num_list.append(value)
print("queue is:", num_list)

for x in range(10):
    y = num_list.pop(0)
    print("current Number is", y, "and the queue is", num_list)

print("The queue is now empty")