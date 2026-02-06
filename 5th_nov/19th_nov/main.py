# Input:
# x = [1,2,3,4,5,6], k = 2
# Output:
# [5, 6, 1, 2, 3, 4]

x = [1,2,3,4,5,6]
k = 4
new=[]
for i in range(-k,len(x)-k,+1):
    new.append(x[i])
print(new)    
# x = [0,1,0,3,12,0,5]
# Output:
# [1,3,12,5,0,0,0]
new=[]
new1=[]
for i in range(len(x)):
    if x[i]==0:
        new.append(x[i])
    else:
        new1.append(x[i])
print(new1+new) 
 # Input:
x = [2,7,11,15,3,6]
target = 9
# Output:
# (2,7) and (3,6)
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]+x[j]==target:
             print(f"{x[i]},{x[j]}")
    
# Find the 3rd largest number WITHOUT sorting
# Input:
# x = [5,9,1,3,7,8,2]
# Output:
# 3rd largest = 7
    
new=[]
for i in range(len(x)):
    for j in range(len(x)):
        if x[i] < x[j]:
            x[i],x[j]=x[j],x[i]
print(x) 

# Check if list is palindrome
# Input:
x = [4,5,6,7,6,5,8]
# Output:
# True
res=[]
a=True
for i in range(len(x)-1,-1,-1):
    res.append(x[i])
    for i in range(len(res)):
        if res[i]==x[i]:
            a=True
            






















    
