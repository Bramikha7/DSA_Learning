# level up q
x="coding"
y="coding"
count=0
if len(x)!=len(y):
    print("invalid input")
else:
    for i in range(len(x)):
        if x[i] not in y[i]:
            count=count+1
    if count ==1:
        print("yes")
    else:
        print("No")

# Given two arrays:
# names → list of student names
# birthdates → list of dates in "dd/mm" format
# Write a program that prints the names of students who were born between January and June (both months inclusive).
# Hint: Use split() to extract day and month.
# Sample Test Case:
# names = ["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"]
# birthdates = ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"]
# Output:
# ['Arun', 'Cathy', 'David', 'Farhan', 'Gita']
# For example:
# TestResultborn_in_first_half(["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"], ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"])
# ['Arun', 'Cathy', 'David', 'Farhan', 'Gita']         

names = ["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"]
birthdates = ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"]
month=[]
for i in birthdates:
    day=i.split("/")
    month.append(day)
new=[]    
for i in range(len(month)):
    new.append(month[i][1])
result=[]    
for i in range(len(new)):
    if new[i]>="01" and new[i]<="06":
        result.append(names[i])
print(result)
