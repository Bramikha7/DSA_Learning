# reverse the list of numbers
input=[10,20,50,99]   
new=[]
for i in range(len(input)-1,-1,-1):
    new.append(input[i])
    print(i, ",", new)
print(new)  

# print the even numbers
input=[2,3,6,8,9]
new=[]
for i in range(len(input)):
    if input[i]%2==0:
        new.append(input[i])
print(new) 

# square the numbers
input=[2,5,8,9]
new=[]
for i in range(len(input)):
    new.append(input[i]*input[i])
print(new)   

# replace the zero for the negative number
input=[5, -3, 9, -8, 2]
new=[]
for i in range(len(input)):
    if input[i] >=0:
        new.append(input[i])
    else:
        new.append(0)
print(new)

# count the len of the given list
input=['apple', 'banana', 'cherry', 'date']
count=0
for i in range(len(input)):
    count=count+1
print(count) 

# print the first negative number
input=[5, 12, 3, -8, 15, -2]
new=0
for i in range(len(input)):
    if input[i]<=0:
        new=(input[i])
        break
print(new)

# sum of the numbers in list
input=[10,20,30,40]
new=0
for i in range(len(input)):
    new=new+input[i]
print(new)  

# Add All Positive Numbers Only
input=[10,-2,9,-7,3]
new=[]
for i in range(len(input)):
    if input[i]>=0:
        new.append(input[i])
print(new)   

# * Electricity Usage Check
# Given a list of daily electricity usage (in units) for a week, print "Power Saving" if all values are below 100,
# otherwise print "High Usage Detected".(Hint: create a new variable called count,check if every element in the element is more than 100, 
# if more than 100, increment the count ,do this till end of the list finally check if count is greater than zero
# if yes, print "High Usage Detected",else, print "Power Saving")

input=[80, 95, 90,110, 85, 70, 88]
count=0
x=""
for i in range(len(input)):
    if input[i]>=100:
        count=count+1
    if count>0:
        x="High usage detected"
    else:
        x="power saving"
print(x)        

# Count Elements Greater Than 50
input= [20, 60, 75, 45, 90, 35]     
count=0
for i in range(len(input)):
    if input[i]>=50:
        count=count+1
print(count)        

# Count Occurrences of a Given Number
input=[3, 5, 3, 8, 3, 9]
target=3
count=0
for i in range(len(input)):
    if input[i]==target:
        count=count+1
print(count)    

# Remove Specific Value Occurrences (Without remove() or pop())
input=[1, 5, 2, 5, 3, 5]
target=5
new=[]
for i in input:
    if i!=target:
        new.append(i)
print(new)  

# Given a list of four or more elements, determine if every element in the list is exactly the same value.
input=['A','A','A','A','A']
uniform=True
for i in range(len(input)):
    if input[i]!=input[0]:
        uniform=False
        break
if uniform:
    print("uniform")        
else :
    print("mixed") 

# Given a list of positive integers,
input=[5, 12, 100, 45, 9, 201]
new=[]
for i in input:
    if i>=10 and i<=99:
        new.append(i)    
print(new)   

# Total Number of Students Passed
input=[25, 65, 78, 39, 56, 41]
count=0
for i in range(len(input)):
    if input[i]>=40:
        count=count+1
print(count)       

# Replace Negative Numbers
input=[-2, 5, -9, 8, 0, -4]
new=[]
for i in range(len(input)):
    if input[i]>=0:
        new.append(input[i])
    else:
        new.append(0)
print(new)    

# Highest Rainfall Day
input=[22, 45, 38, 55, 41, 35, 29]
new=input[0]
day=1
for i in range(len(input)):
    if input[i]>new:
        new=input[i]
        day=i+1
print("day",day)    

# Product of All Number
input=[1, 2, 3, 4]
new=1
for i in range(len(input)):
    new=new*input[i]
print(new)   


