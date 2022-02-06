# div.py
# input numbers and run caculation
# Author Michael Casey


#collecting number from users
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

#running calculation
ans = int(x/y)

#finding remainder
rem = x%y

#testing asnwer
print (ans)
print (rem)

print ("{} divided by {} is {} with remainder {}".format(x,y,ans,rem))