input= "Python makes programming enjoyable"
new=" "
res=[]
for i in range(len(input)):
    if input[i]!=" ":
        new=new+input[i]
    else:
        res.append(new)
        new=" "
res.append(new)
count=0
result=" "
for i in res:
    if len(i)> count:
        count=len(i)
        result=i
print(result)        
    
