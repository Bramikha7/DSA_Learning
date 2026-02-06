#  Write a function that merges two lists by taking elements alternately.

x= [1, 2, 3] 
y= ['a', 'b', 'c']
new=[]
for i in range(len(y)):
    new.append(x[i])
    new.append(y[i])
print(new)    


# Write a Program that Keep Words That Start and End With the Same Letter

x=["level", "Apple", "mana", "cool"]
new=[]
for i in x:
    if i[0]==i[-1]:
        new.append(i)
print(new) 



