input="Python is super powerful"
new=""
result=[]
for i in range(len(input)):
    if input[i]!=" ":
        new+=input[i]
    else:
        result.append(new)
        new=""
result.append(new) 
print(result)
res=result[0]
for el in result:
    if len(el)< len(res):
        res=el
print(res)

x=[1,3,5,7]
a = True

for i in range(len(x)-1):
    if x[i] >= x[i+1]:
        a = False 
        break
print(a) 

x="abcdefg"
new=""
output= gbecdfa
res=""
for i in range(len(x)):
    if i%2==0:
        res = x[i] + res
    else:
        new = new + x[i]
result=res+new
print(result)    

# Replace characters at odd indexes with *.
n= "hello"
result="" 
for i in range(len(n)):
    if i%2!=0:
        result=result+"*"
    else:
        result+=n[i]
print(result)  

n= "Hello World Python"
new=""
for i in range(len(n)):
    if n[i]!=" ":
        new=new+n[i]
print(new)        
       

    


            
          