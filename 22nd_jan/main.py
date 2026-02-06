# Write a python script to reverse the words in a given sentence.
# Input -> “Abc def”
# Output -> “cbA fed”
input="Abc def"
new=""
res=[]
for i in range(len(input)):
    if input[i]!=" ":
        new=new+input[i]
    else:
        res.append(new)
        new=""
res.append(new)
result=""
new1=""
for el in res:
    for i in range(len(el)):
        result=el[i]+result
    new1=new1 + result+" "   
    result=""
print(new1)    

# Write a python script to print the occurrences of a given letter in a word.
# Input -> word -> “Mississippi”, letter -> “s”
# Output -> 4
input="Mississippi"
letter="s"
count=0
for i in range(len(input)):
    if input[i]==letter:
        count=count+1
print(count)  

# Write a function to check whether a word is the same when read backward.
#   (Bonus: Don’t use slicing or built-ins — use loops only.)
# Print "Yes", if found matching,Print "No", if not matching
# Input: word = "level" Output: Yes
# Input: word = "section", Output: No

input="level"
new=""
for i in range(len(input)):
    new=input[i]+new
if new==input:
    print("yes")
else:
    print("No")    


# Given a list of numbers,first calculate the average of all the numbers.Then, create and print a 
# new list where each element is the difference between the original number and the calculated average.
# Sample Input: [10, 20, 30]
# Expected Output: [-10.0, 0.0, 10.0]
# (The average is 20.0. Calculated as: 10-20, 20-20, 30-20)

input=[10,20,30]
sum=0
avg=0
new=[]
for i in range(len(input)):
    sum=sum+input[i]
avg=sum/len(input)

for i in input:
    a=i-avg
    new.append(a)
print(new)

  
#Square Each Number in a List
#   Write a Python program to create a new list that contains the squares of all numbers from a given list.
# ```python
# Input: [2, 3, 4, 5]
# Output: [4, 9, 16, 25]
 
input=[2,3,4,5]
res=[]
for i in input:
    new=i**2
    res.append(new)
print(res)    

#Count Occurrences of a Given Number
#   Write a program to count how many times a specific number appears in a list.
# ```python
# Input: numbers = [3, 5, 3, 8, 3, 9], target = 3
# Output: 3
# ```
input=[3, 4, 3, 8, 4, 9]
target=3
count=0
for i in range(len(input)):
    if input[i]==target:
        count=count+1
print(count)  

# Replace Negative Numbers with 0
#   Write a program that replaces all negative numbers in a list with 0.
# ```python
# Input: [5, -3, 9, -8, 2]
# Output: [5, 0, 9, 0, 2]
input=[5,-3,9,-8,2]
new=[]
for i in range(len(input)):
    if input[i]<0:
        new.append(0)
    else:
        new.append(input[i]) 
print(new) 

# Count Elements Greater Than 50
#   Given a list of numbers, count how many numbers are greater than 50.
# ```python
# Input: [20, 60, 75, 45, 90, 35]
# Output: 3
input=[20, 60, 75, 45, 90, 35]
count=0
for i in range(len(input)):
    if input[i]>50:
        count=count+1
print(count) 

# Sum of First and Last Elements
# Write a program to find the sum of the first and last elements of a list.
# ```python
# Input: [10, 20, 30, 40, 50]
# Output: 60  # (10 + 50)
# ```
input=[10, 20, 30, 40, 50]
new=0
for i in range(len(input)):
    new=(input[0]+input[-1])
print(new)
    
# Write a program to print each element along with its index position.
# ```python
# Input: ["apple","banana","grapes"]
# Output:
# Index 0 apple
# Index 1 banana
# Index 2 grapes
input=["apple","banana","grapes"]
for i in range(len(input)):
    print("index",i,"input",input[i])

#  Find Sum of Odd and Even Numbers Separately
#   Write a program that finds the sum of all odd numbers and even numbers in a list separately.
# ```python
# Input: [10, 15, 20, 25, 30]
# Output: even_sum = 60, odd_sum = 40
input=[10, 15, 20, 25, 30]
even_sum=0
odd_sum=0
for i in range(len(input)):
    if input[i]%2==0:
        even_sum=even_sum+input[i]
    else:
        odd_sum=odd_sum+input[i]
print("even_sum:",even_sum,"odd_sum:",odd_sum)            

# Replace All Negative Numbers with Zero
# Write a program to replace every negative number in a list with 0.
# ```python
# Input: [10, -5, 20, -10, 30]
# Output: [10, 0, 20, 0, 30]
# Hint: change every negative with zero number
# use the index and change . for example -> x[index] = 0
# ```
input=[10, -5, 20, -10, 30]
new=[]
for i in range(len(input)):
    if input[i]<0:
        new.append(0)
    else:
        new.append(input[i]) 
print(new) 

