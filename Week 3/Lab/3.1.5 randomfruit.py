# randomgenerator.py
# picks a random fruit from the list
# Author Michael Casey

#import random
import random

#create a list of fruits
list = ['apple', 'bannana', 'pear', 'grapes']

index = random.randint(0,len(list)-1)


#print (index)

fruit = list[index]
print ("A random fruit: {}".format(fruit))