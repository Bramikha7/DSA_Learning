# Traverse
input=[[1,2,3],[4,5,6],[7,8,9]]
m=[]
for i in range(0,len(input),+1):
    n=[]
    for j in range(0,len(input[i]),+1):
        n.append(input[j][i])
    m.append(n)
print(m)   

# matrix
input=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(input),+1):
    for j in range(0,len(input[i]),+1):
        print(input[i][j])