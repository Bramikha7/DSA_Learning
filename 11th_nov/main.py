
# odd number count
num_x=[1,2,3,4,5,6,7]
num_y=[11,22,33,44,55]
x=0
y=0
for i in num_x:
    if i%2!=0:
        x=x+1
for j in num_y:
    if j%2!=0:
        y=y+1
if x>y:
    print(num_x)
elif x<y:
    print(num_y)
else:
    print("Both are equal")


# divisible by previous number
num=[1,2,4,6,8]
new=[]
for i in range(1,len(num)):
    if num[i]%num[i-1]==0:
        new.append(num[i])
print(new)   

# remove the last value by k
num=[10,20,30,40,50]
k=2
new=[]
if k >len(num):
    print("invalid input")
else:
    for i in range(len(num) -k):
        new.append(num[i])
    print(new)    

# remove the value of k (front)
num=[1,2,3,4,5,6]
k=3
new=[]
for i in range(k, len(num)):
    new.append(num[i])
print(new)

# previous greatest number
input=[5,6,2,9,12,8]
new=[]
for i in range(len(input)):
    if input[i]>input[i-1]:
        new.append(input[i])
print(new) 

# next  number divisible
input=[8,4,2,1]
new=[]
for i in range(len(input)-1):
    if input[i]%input[i+1]==0:
        new.append(input[i])
print(new)   

# print even numbers 0
input=[1,2,3,4,5,6]
new=[]
for i in range(len(input)):
    if input[i]%2==0:
        new.append(0)
    else:
        new.append(input[i])
print(new)

# remove the value of k infront of list and attach it back
input=[1,2,3,4,5,6]
k=2
new=[]
for i in range(k,len(input)):
    new.append(input[i])
for i in range(k):
    new.append(input[i])
print(new)    

























