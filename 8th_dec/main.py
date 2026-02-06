input="Ram!_kumar@2025"
result=""
num="1234567890"
letter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for el in input:
    if el=="_" or el in num:
        result=result+el
    if el in letter:
        result=result+el.lower()
print(result) 

x="ab#21!cd@EF3"
new=""
num="1234567890"
alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for el in x:
    if el in alp:
        new=new+el.upper()
    if el in num:
        new=new+el
print(new) 

n="for, people: group!"
result=""
alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="1234567890"
for el in n:
    if el==" " or el in alp or el in num:
        result=result+el
print(result)  

word="hheyyyyy"
count=0
res=""
for i in range(len(word)):
    for j in range(i+1,len(word)):
        if word[i]==word[j]:
            count=count+1
    if count<1:
        res=res+word[i]
    count=0
print(res) 

