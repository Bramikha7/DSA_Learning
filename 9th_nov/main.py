# Increase Every Element by 10
input=[2, 4, 6, 8]  
new=[]
for i in range(len(input)):
    new.append(input[i]+10)
print(new)  

# Sum of First and Last Elements
input=[20,30,40,10,50]
new=0
for i in range(len(input)-1,3,-1):
    new=(input[i]+input[0])
print(new)

# Find Index of an Element (Without using index())
input=[11, 22, 33, 44, 55]
search=33
new=0
for i in range(len(input)):
    if input[i]==search:
        new=i
print(new)

# Write a program to print each element along with its index position.
input=["apple","banana","grapes"]
for i in range(len(input)):
    print("index:",i,"input:",input[i]) 

# Find the Sum of All Numbers (Without Using sum())
input=[2, 4, 6, 8]
new=0
for i in range(len(input)):
    new=new+input[i]
print(new)        

# Find Sum of Odd and Even Numbers Separately
input= [10, 15, 20, 25, 30]
even_no=0
odd_no=0
for i in range(len(input)):
    if i%2==0:
        even_no=even_no+input[i]
    else:
        odd_no=odd_no+input[i]
print("even=",even_no, "odd_no=",odd_no)  

# Replace All Negative Numbers with Zero
input=[10, -5, 20, -10, 30]
new=[]
for i in range(len(input)):
    if input[i]>=0:
        new.append(input[i])
    else:
        new.append(0) 
print(new)           

# Vowel Extractor
input="education"
new=[]
vow="aeiouAEIOU"
for i in range(len(input)):
    if input[i] in vow:
        new.append(input[i])
print(new)        

# Find Word with Maximum Vowels
input=["cat", "eagle", "umbrella", "sky"]
new=0
count=0
word=" "
vow="aeiou"
for i in range(len(input)):
    for j in input[i]:
        if j in vow:
            count=count+1
    if count>new:
        new=count
        word=input[i]
print(word)                 

# palindrome
input="amma"
new=""
for i in range(len(input)):
    new=input[i]+new
print(new)
if new==input:
    print("True")
else:
    print("False")


# reverse
input="python"
new=" "
for i in range(len(input)-2,0,-1):
    new=new+input[i]
print(new)

# first and last index
input=[5, 2, 3, 5, 7, 5, 8] 
key= 5
new=[]
for i in range(len(input)):
    if input[i] == key:
        new.append(i)
    print("Firstindex:",new[0] "lastindex:",new[-1])     

# Combine Two Lists Alternately
new1=[10, 20, 30]
new2=[1, 2, 3]
new=[]
for i in range(len(new1)):
    new.append(new1[i])
    new.append(new2[i])
print(new)    


                



