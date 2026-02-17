n=3
for i in range(1,n+1):
    print(i,"=>",end=" ")
    for j in range(1,n+1):
        print(j,end=" ")
    print()     

n=3
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()        

n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    

n=4
for i in range(1,n+1):
    space=n-i 
    print(" "*space,end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()  

n=4
for i in range(n,0,-1):
    space=n-i
    print(" "*space,end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
n=3
for i in range(-1,n+1):
    space=n-i
    print(" "*space,end=" ")
    for j in range(1,i+3):
        print(j,end=" ")
    print()  