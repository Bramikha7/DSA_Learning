# 1
Output: [3,11,4,6,9,2]

nums = [4,6,9,2,3,11]
k = 2

new=[]
result=nums[-k:]
for i in range(0,len(nums)-k):
    new=result
    new.append(nums[i])
print(new)

# # 2
nums = [4,2,7,2,9,3,2,8]
k = 2
new=[]
for i in range(len(nums)):
    if nums[i]==k:
        new.append(i)
print(new)        
# # 3
nums = [1,3,7,8,9]
new=[]
for i in range(len(nums)-1,-1,-1):
    new.append(nums[i])
print(new)  
# # 4
input="HelloWorld"
count=0
alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0,len(input),+1):
    if input[i] in alp:
        count += 1
print(count)
# # 5
input="Johannesburg is the most populous city of South Africa"
new=""
result=[]
for i in range(len(input)):
    if  input[i]!=" ":
        new+=input[i]
    else:
        result.append(new)
        new=""
result.append(new)
max=0
res=""
for i in result:
    if len(i)>max:
        max=len(i)
        res=i
print(res)

# # 6
input= "apple and banana"
new=" "
result=[]
res=" "
for i in range(len(input)):
    if input[i]!=" ":
        new+=input[i]
    else:
        result.append(new)
        new=" "
result.append(new)
for i in result:
    res=i+res
print(res)

arr = [1, 2, 4, 6, 7, 9]
N = 10
new=[]
for i in range(1,N+1):
    if i not in arr:
        new.append(i)
print(new)    

input = "Anna went to America and met Adam"
count=0
new=""
result=[]
for i in range(len(input)):
    if input[i]!=" ":
        new+=input[i]
    else:
        if new[0].upper()==new[-1].upper():
            count+=1
        new="" 
    print("Count:",count)           
        result.append(new)
        new=" "
result.append(new)
print(result) 
for i in result:
    for j in range(0,len(i),+1):
        if j[0]==j[-1]:
            count=count+1
print(count)                   

for i in range(0,len(x),+1):
    print(x[i])
    if x[0] == "a":
        print(x[i])
        result.append(x[i])
print(result)        








