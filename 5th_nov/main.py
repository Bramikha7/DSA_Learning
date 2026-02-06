
# duplicate 
def element(n):
    numbers=[]
    for i in n:
        if i not in numbers:
            numbers.append(i)
    print(numbers)        
element([1,2,3,4,2,4]) 

# second largest number

def largest(n):
    one=n[0]
    two=n[0]
    for i in n:
        if i >=one:
            one=i
    for i in n:
        if i>two and i!=one:
            two=i
    print(two)        
    
    
largest([75,80,90,100])
    

