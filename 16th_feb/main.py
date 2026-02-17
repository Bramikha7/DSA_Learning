input=[20,30,15,44,77]
min_value=input[0]
max_value=input[0]
for el in input:
    if el>max_value:
        max_value=el
    elif el<min_value:
        min_value=el
print(max_value,min_value)     