input="Data science evolves every year"

new=" "
res=[]
for i in range(len(input)):
    if input[i]!=" ":
        new=new+input[i]
    else:
        res.append(new)
        new=" "
res.append(new)
max=0
result=" "
for i in res:
    if len(i)>max:
        max=len(i)
        result=i
print(result)        

# # Write a Python program to find the word that has maximum number of vowels from the given sentence

input="Learning Python is interesting bow "
new=" "
res=[]
for i in range(len(input)):
    if input[i]!=" ":
        new=new+input[i]
    else:
        res.append(new)
        new=" "
res.append(new)
result=""
max=0
vow="aeiou"
for i in res:
    count=0
    for j in i:
        if j in vow:
            count=count+1
    if count>max:
        max=count
        result=i
print(result)   

# Write a python program to find the words that has more than 4 characters

input="This is a python program"
k=4
new=input.split()
# res=[]
# for i in range(len(input)):
#     if input[i]!=" ":
#         new=new+input[i]
#     else:
#         res.append(new)
#         new=" "
# res.append(new)
for el in range(len(new)):
    if len(new[el])>k:
        print(new[el])
        
               


