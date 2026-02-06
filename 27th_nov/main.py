# Rearrange by Length
# Given a list of words, rearrange them so shorter words come first.
#  (Don't use sort() or sorted())
#  x=["banana", "cat", "watermelon", "apple"]
# Output:
#  ["cat", "apple", "banana", "watermelon"]
x = ["banana", "cat", "watermelon", "apple"]
new = []

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if len(x[i])> len(x[j]):
            temp=x[i]
            x[i] = x[j]
            x[j]=temp       
    
print(x)

# Words Ending in "ing"
# Input:
# ["playing", "run", "walking", "see", "coding"]
# Expected Output:
# ["playing", "walking", "coding"]

x=["playing", "run", "walking", "see", "coding"]
new=[]
for i in x:
    if i[-3:-1] in"ing":
        new.append(i)
print(new)  

# a list of students
# a list of scores (same length)
#  Return the names of students whose name has more than 3 vowels AND whose score is above average score.
#  Use nested loops (one to count vowels, one to compute average).
# Input:
#  students = ["Aravind", "Bala", "Eeshwar", "Louis", "Gita"]
#  scores = [85, 70, 92, 88, 60]
# Output:
#  ["Aravind", "Eeshwar", "Louis"]
x=["Aravind", "Bala", "Eeshwar", "Louis", "Gita"]
y=[85, 70, 92, 88, 60]
vow="aeiou"
new=[]
count=0
for i in range(len(x)):
    if x[i] in vow:
        count=count+1
        if count>=3:
            new.append(x[i])   
print(new)            

# Given a list and a target value, return all indices where the target appears.
#  Example: [1, 2, 3, 2, 4, 2] → target 2 → indices [1, 3, 5].
x= [1, 2, 3, 2, 4, 2]
target=2
new=[]
for i in range(len(x)):
    if x[i]==target:
        new.append(i)
print(new)   

# Reverse Every Word but Keep the Sentence Order
# Given a sentence, reverse each word individually, but keep the 
# word order unchanged.
 # Example: "hello world" → "olleh dlrow".
new= "hello world"
a=""
b=[]
for i in new:
    if i != " ":
        a = i + a
    else:
        b.append(a)
        a=" "
b.append(a) 
print(b)

 # Print numbers where sum of first and last digit is prime.
# Input: [42, 57, 88, 91]
 # Output: 42 57
 # (4+2=6 not prime, 5+7=12 not prime… only primes printed.)
n = [42, 58, 88, 91]

for num in n:
    first = int(str(num)[0])
    last = num % 10
    s = first + last
    if s <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, s):
            if s % i == 0:
                is_prime = False
                break
    if is_prime:
        print(num)