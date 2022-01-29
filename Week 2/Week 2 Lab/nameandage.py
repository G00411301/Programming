# nameandage.py
# reads name and age input and prints
# Author Michael Casey G00411301

name = input ('What is your name?')
age = int(input ('How old are you?'))
age2 = age - 4
#print ('Hi {},' '\tyour age is {}' .format(name,age))
print ('Hi {},' '\tyour age is {}, four years ago you were {}' .format(name,age,age2))
