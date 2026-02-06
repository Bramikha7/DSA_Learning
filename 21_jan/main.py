# Write a function that prints the first and last characters of a given string
input="hello world"
for i in range(len(input)):
    if i==0 or i==len(input)-1:
        print(input[i])

# Write a function that counts how many vowels are present in the string. 
n="hello world"
vow="aeiou"
count=0
for i in range(len(input)):
    if input[i] in vow:
        count=count+1
print(count)

# Write a function that takes a sentence and counts how many “words” it has (words are separated by spaces).  
# count_words("Python is fun")  -> 3
# count_words("I love programming in Java") -> 5
x="python is fun"
count=0
new=""
res=[]
for i in range(len(x)):
    if x[i]!=" ":
        new=new+x[i]
    else:
        res.append(new)
        new=""
res.append(new)
print(len(res))   

# Write a function that replaces every vowel in a string with the symbol `-`.
# replace_vowels(“banana”) -> b-n-n-
# replace_vowels(“arrow”) -> “-rr-w”

y="banana"
vow="aeiou"
new=""
for i in range(len(y)):
    if y[i] in vow:
        new=new+"-"
    else:
        new=new+y[i]    
print(new)

# Write a function that takes a string and returns a **new string with all vowels removed**.
# new_string(“education”) -> “dctn”
# new_string(“academy”) -> “cdmy”

res="education"
vow="aeiou"
new=""
for i in range(len(res)):
    if res[i] not in vow:
        new=new+res[i]
print(new) 

# Write a python script to drop all the numbers from the given string 
# Input -> “He12llo, Py00th55on”
# Output -> “Hello, Python”
result="he12llo, py00th55on"
num="1234567890"
new_s=""
for i in range(len(result)):
    if result[i] not in num:
        new_s=new_s+result[i]
print(new_s)   