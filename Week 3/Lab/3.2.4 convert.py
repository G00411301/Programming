#convert.py
# converts a float to an absolute, converts dollars and cetns to dollars
# Author Michael Casey

#gater input amount
value = float(input("Please enter an amount: "))

#convert value to ansolute value
absolutevalue = abs(value)

#inout is now an absoute value, in order to convert it to cent, multiply in by 100
output = absolutevalue * 100

#print the result to screen
print ("That amount in cent is: {}".format(int(output)))

#testing output
#print (absolutevalue)