#normalise.py
#reads in a string and strips any leading or trailing spaces, the program should also convert the string to lower case
#Michael Casey

rawstring = input("Please enter a string: ")
normailisedstring = rawstring.strip() .lower ()

#print (normailisedstring)

length1 = len(rawstring)
length2 = len(normailisedstring)

print ("That string normalised is {}".format(normailisedstring))
print ("We reduced the input string from {} to {} characters".format(length1,length2))