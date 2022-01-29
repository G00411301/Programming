#multiply.py
# This program muliplies 111 by 555 and displays the answer
# Author Michael Casey G00411301

# The original code from the lab - answer = 111 * 555 - does not work as it is only assigning a 
# value to the input "answer", this would work if the code was amended as follows:
#answer = 111 * 555
#print (answer)

#Assigning names to values to call

Value1 = 111
Value2 = 555
answer = Value1 * Value2

#Simply oututs the result of 111 * 555
#print (Value1 * Value2)

#Print answer using input values
#print (answer)


#Improves the appearance of above
print ('The answer of {} multiplied by {} is {}'.format (Value1, Value2, answer))