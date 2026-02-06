# Given a list of words,print only the ones that start with an uppercase letter. Use a single loop to check their first character

x=["Apple","ball","Cat","dog"]
new=""
res="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(x)):
    if (x[i][0]) in res:
        new=new+" " +x[i]
print(new)

# print the score which is above 80 in both list
maths=[92,45,81]
sci=[88,90,70]
new=[]

for i in range(len(maths)):
    if int(maths[i])>=80 and int(sci[i])>=80:
        new.append(i)
print(new)    

# filter numbers satisfying 3 conditions 
# 1. are 4 digits
# 2. end with an even digit

x=[2481,3572,602,7890,4214]
new=[]
for i in range(len(x)):
    if int(x[i])>1000 and int(x[i])<9999:
        if x[i]%2==0:
            new.append(x[i])
print(new)        

# From a string, collect all the lowercase letters in the same order.
#   Use a single loop to scan the string.

x="PyTHonProGRam"
res=""
small="abcdefghijklmnopqrstuvwxyz"
for i in range(len(x)):
    if (x[i]) in small:
        res=res+x[i]
print(res)   

# you are given a list containing integers, floats and strings.
# Create a new list containing only the float values using one loop.

x=[10, 3.5, "hello", 8.2, 6]
new=[]
for i in x:
    if type(i)==float:
       new.append(i)
print(new)

#  Given two strings, S_1 and S_2, determine if S_2 is a rotation of S_1.
#   For example, "waterbottle" is a rotation of "erbottlewat".
#   Assume both strings have the same number of characters. Print True or False.

x= "ABCDE"
y="CDEAB"

if len(x)==0 or len(y)==0:
    print("Invalid")
else:
    final=x
    output=False
    for i in range(0,len(x),+1):
         temp=final[1:]+final[0]
         final=temp
         if final==y:
             output=True
    print(output) 

# Keep Words With No Repeated Letters
def equal(x):
    new= []
    for i in x:
        b = ""
        for el in i:
            if el not in b:
                b += el
        if len(b) == len(i):
            new.append(i)
    print(new)
equal(["hello","python","jav","alice"])

# Filter numbers whose reverse is greater than the number.
# Given a list of integers, print only those numbers whose reversed value is greater than the original number.
