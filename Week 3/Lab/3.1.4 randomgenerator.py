# randomgenerator.py
# input numbers and run caculation
# Author Michael Casey

import random

#added ability for user to input range
x = int(input("What is the first number in the range: "))
y = int(input("What is the last number in the range: "))

num = random.randint(x,y)
print ("The random number between {} and {} is {}".format(x,y,num))
#print (" Here is the random number {}".format(num))