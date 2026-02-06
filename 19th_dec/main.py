# PET Practice problems:
# Question 1: Remove Duplicates from a String
# Problem Statement
# You are given a string that may contain repeated characters.
#  Write a Python program to remove all duplicate characters from the string and return a new string that contains only the first occurrence of each character, while preserving the original order.
# Input
# input="A single string s containing letters, digits, or symbols."
# Output
# A string with duplicate characters removed.
# Sample Input

# input="programming"
# Sample Output

# progamin
# Explanation
# The characters r, g, and m appear more than once.
# Only their first occurrence is kept.
# Order of characters remains the same as the input.
new=""
for i in range(len(input)):
    for j in range(len(input)):
        if input[j] not in new:
            new=new+input[j]
print(new)            

# Find the Longest Word in a Sentence
# Problem Statement
# You are given a sentence consisting of multiple words separated by spaces.
#  Write a Python program to find and print the longest word in the sentence.
# If two or more words have the same maximum length, print the first occurring word.
# Input
# A single line string representing a sentence.
# Output
# The longest word in the sentence.
# Sample Input

# input="Python programming is very interesting"
# Sample Output

# programming
# Explanation
# Word lengths:
# Python → 6
# programming → 11
# is → 2
# very → 4
# interesting → 11
# programming appears first among the longest words.

new=[]
res=""
for i in range(len(input)):
    if input[i]!=" ":
        res=res+input[i]
    else:
        new.append(res)
        res=""
new.append(res)
print(new) 
max=0
temp=""
for i in new:
    if len(i)>max:
        max=len(i)
        temp=i
print(temp)  


# Count Occurrences of a Substring
# Problem Statement
# You are given a string and a substring.
#  Write a Python program to count how many times the substring appears in the given string.
# Overlapping occurrences should also be counted.
# Input
# A string main_string
# A string sub_string
# Output
# An integer representing the number of occurrences of the substring.
# Sample Input

# Main_String="ababab"
# Substring= "aba"
# # Sample Output

count=0
for i in range(0,len(Main_String)):
    for j in range(i,len(Main_String)):
        temp=Main_String[i:j+1]
        if temp==Substring:
            count+=1
print(count)

# 2

# Count the number of digits of a given number N.
# Size of the integer ranges from 1<N<100000.
# NO STRINGS CONVERSIONS ALLOWED.
# Sample Input:
# input=548
# Sample Output:
# 3
# Explanation:  three digits allowed

# print(5432%10)#it's get the last digit
# print(5432//10)#It's remove the last digit
# count=0
# while input>0:
#     input=input//10
#     count=count+1
# print(count)    
    
input="python is programming language"
words=input.split(" ")
print(words)
new=[]
res=""
for i in range(0,len(input)):
    if input[i]!=" ":
        res=res+input[i]
    else:
        new.append(res)
        res=""
new.append(res)
print(new)
temp=""
for el in new:
    el=el[0].upper+el[1:]
    temp=temp+el
print(temp)    
    