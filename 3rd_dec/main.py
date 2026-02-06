# Given an array count the number of elements higher than the average of the array?
# Assume all the elements inside the array are greater than zero. 
# Bonus: If validation for the input array is possible, you can include 


input=[5,5,5,5,5]
sum_avg=0
new=0
res=input[0]
count=0
for i in range(len(input)):
    sum_avg=sum_avg+input[i]
    new=sum_avg/len(input)
for el in input :
    if el > new:
        count+=1
print(count)  

#  Write a Python program to remove all duplicate characters from a given string and return the result.
#   The final string should contain only the first occurrence of each character, in the same order.


input= 'programming'
new=input[0]
res=" "
for i in range(len(input)):
   if input[i] not in res:
       res=res+input[i]
print(res)

# Write a Python program to find and print the longest word in a given sentence.

input= "Python makes programming enjoyable"
new=" "
res=[]
for i in range(len(input)):
    if input[i]!=" ":
        new=new+input[i]
    else:
        res.append(new)
        new=" "
res.append(new)
count=0
result=" "
for i in res:
    if len(i)> count:
        count=len(i)
        result=i
print(result)        
    
