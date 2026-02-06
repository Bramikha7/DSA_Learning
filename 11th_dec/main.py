1.Print numbers that appear more than once (duplicates only)
input= [1,4,2,7,4,1,8,2,2]
 Output → 1, 2, 4
new=input[0]
res=[]
for i in range(len(input)):
    for j in range(i+1,len(input)):
        if input[j]==input[i]:
            print(input[i])  


.Reverse only the words, not the whole sentence
input= "I love python"
 Output → "I evol nohtyp"
new=""
res=[]

for i in range (len(input)):
    if input[i]!=" ":
        new=new+input[i]
    else:
        res.append(new) 
        new=" "
res.append(new)
result=""
new1=""
for el in res:
    for i in range(len(el)):
        result=el[i]+result
    new1=new1+result+" "
    result=""
print(new1)   

         

Count pairs where the second number is bigger
Test case 1:
input =[1, 5, 2, 6, 3, 9]
Output # 3   

odd=[]
even=[]
count=0
for i in range(len(input)):
    if i%2==0:
        even.append(input[i])
    else:
        odd.append(input[i])
for i in range(len(even)):
    if even[i]<odd[i]:
        count=count+1
print(count)     

Rotate a list to the right by 1 step (no slicing)
input= [1,2,3,4,5]
res=[]
 Output: [5,1,2,3,4] 
for i in range(-1,len(input)-1):
    res.append(input[i])
print(res)    
Count How Many Numbers Are Greater Than the Average
You are given a list:

input=[4, 8, 1, 9, 3, 10, 5]
sum=0
count=0
for i in range(len(input)):
    sum=sum+input[i]/len(input)
    if input[i]>sum:
        count=count+1
print(count)    

 Given a sentence, split it into words and return how many words it has.
input="Python is super cool"
Output: 4
words=input.split()
print(len(words))
new=[]
res=" "
for i in range(len(input)):
    if input[i]!=" ":
        res=res+input[i]
    else:
        new.append(res)
        res=" "
new.append(res)
print((len(new)))
Count how many words start with a vowel
Problem:
Use split() to extract words and count the ones starting with a, e, i, o, u.
input="apple is on the orange table"
Output:
3   

words=input.split()
count=0
vow="aeiou"
print(words)
for i in range(len(words)):
    if words[i][0] in vow:
        count=count+1
print(count)        


Count how many words contain digits
input="room1 is bigger than room2 but room3 is small"
#  Output: 3
count=0
num="1234567890"
for i in range(len(input)):
    if input[i] in num:
        count=count+1
print(count)        

input=["1/2", "2/09", "3/06"]
ouput=6

add all dates
imagine first is date second one is month
new=[]
for i in range(len(input)):
    new.append(input[i][0])
print(new) 
res=0
for el in new:
    res=res+int(el)
print(res) 
day=[] 
sum=0 
avg=0
date=[]
month=[]
for el in input:
    days=int(el.split("/")[0])
    months=int(el.split("/")[1])
    date.append(days)
    month.append(months)
    print(day,month)
    print(date)
    print(month)
    for i in range(len(month)):
        sum=sum+month[i]
    print(sum)

# Finding average of 2 lists and printing list with highest average WITHOUT using any library functions.
first_list = [4, 1, 2, 3, 5]
second_list = [1, 0, 0, 1, 2, 1, 0, 2]
# Output:
# [4, 1, 0, 3, 5]
# If both averages are the same, print "Both are equal"   
sum=0
avg=0
avg1=0
sum1=0
for i in range(len(first_list)):
    sum=sum+first_list[i]
for j in range(len(second_list)):
    sum1=sum1+second_list[j]
    avg=sum/len(first_list)
    avg1=sum1/len(second_list)
if avg==avg1:
    print("Both are equal")
elif avg>avg1:
    print(first_list)
elif avg<avg1:
    print(second_list)

# A company keeps two lists:

# One list has employee names.

# Another list has each employee’s shift hours (integer).

# A new project needs employees whose shift hours are strictly between two given limits (lower < hours < upper).
# Your task: return a new list of names that match this rule.
# If no employee qualifies or either list is empty, return ["None"].

# Input:
names = ["Arun", "Beema", "Chandru", "Dev", "Esha"]
hours = [5, 9, 12, 4, 10]
lower = 6
upper = 11

res=[]
if len(names)==0 or len(hours)==0:
    print("None")
else:
    for i in range(len(hours)):
        if lower < hours[i] < upper:
    for i in range(len(hours)):
        if hours[i] > lower and hours[i] < upper:
            print(names[i])

x="i love python"
res=" "
new=" "
for i in range(len(x)):
    if x[i]!=" ":
        res=x[i]+res+" "
    else:
        new=new+res
        res=" "
print(new+res)   

# Find All Pairs That Sum to a Target (without using set or map)
input= [1,5,7,-1,5]
target = 6
#  Output:
#  Pairs: (1,5), (7,-1), (1,5) (count all)

for i in range(len(input)):
    for j in range(i+1,len(input)):
        if input[i]+input[j]==target:
          print((input[i],input[j]),",") 

#  Find the Minimum Element (without inbuilt min)
# Problem:
#  Given an array of integers, find the smallest value using only loops.
# Example:
input= [4, 7, 1, 9, 2]
# #  Output: 1  
count=input[0]  
for i in range(len(input)):
   if input[i]< count:
      count=input[i]
print(count)      
   
# Return the first and last word
input="split makes string handling easy"
# Output:
#  ["split", "easy"] 
new=[]
res=" "  
for i in range(len(input)):
    if input[i]!=" ":
      res=res+input[i]
    else: 
       new.append(res)
       res=" "
new.append(res)
print([new[0],new[-1]])  

# Problem:
#  Given an array, count how many numbers are positive, negative, and zero.
# Example:
input= [-1 ,2, 0, -4, 5, 0]
#  Output:
Positive = 2
Negative = 2
Zero = 2
positive=0
negative=0
zero=0
for i in range(len(input)):
    if input[i]>0:
      positive=positive+1
    elif input[i]<0:
       negative=negative+1
    elif input[i]==0:
       zero=zero+1  
print("positive",positive)
print("negative",negative)
print("zero",zero)               

# Given an array, move all zeros to the end without using extra array.
# Example:
input= [0, 1, 0, 3, 12]
#  Output: 1 3 12 0 0    
new=[]
new1=[]
for i in range(len(input)):
    if input[i]==0:
        new.append(input[i])
    else:
        new1.append(input[i])    
        
print(new,new1)        


















