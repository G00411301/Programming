#floor.py
# takes in a float and outputs an int rounded down
# Author Michael Casey

#importing math module
import math

#take in number from user
num = float(input("Enter a number: "))
#round number down
rnddwn = math.floor(num)

print ("{} rounded down is {}".format (num,rnddwn))