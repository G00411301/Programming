# extra.py
# looking at questions 6, 7 and 8
# Author Michael Casey

#Question 6
from sqlite3 import IntegrityError


message = 'I have eaten ' + str(99) + ' burritos.'
print (message)

#Q6 - 99 is an integer, you can not add a number to a sentence so first you must convert the number to a string for inclusion.


#Question 7
# variable names can not start with a number, they must start with a letter

#Question 8
#int = Integer
# str = string
# float = float

number = 5
print (float(number))