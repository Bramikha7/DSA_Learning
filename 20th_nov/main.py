# A list is strictly increasing if every next element is greater than the previous one.
# Example:
# [1,3,5,9] → True
# [2,2,5] → False (because 2 is NOT less than 2)
# [10,5,6] → False (because 5 < 10)
x=[2,2,5]
a=True
for i in range(1,len(x)):
    if x[i]>x[i-1]:
        a=True
    else:
        a=False
        break
print(a)

# Given 4 arrays, names, maths_marks, physics_marks and chemistry_marks.  Find the names of students who got more than 90 marks 
# in all three marks and print the name of the student who got the highest total among them.

# Print "No student found" if there are no students how have score more than 90 in all 3 subjects. 

# For example:

# Test	Result
# highest_marks(["jason", "priya", "madhan", "syed"], 
#               [91, 92, 81, 75],
#               [91, 89, 100, 90],
#               [91, 95, 100, 90])





# Reverse Words But Not Letters Inside
input= "I love Python"
 # Output: "Python love I"
new=" "
result=[]
res=" "
for i in range(len(input)):
    if input[i]!=" ":
        new+=input[i]
    else:
        result.append(new)
        new=" "
result.append(new)
for i in result:
    res=i+res
print(res)

# Given 4 arrays, names, maths_marks, physics_marks and chemistry_marks.  
# Find the names of students who got more than 90 marks in all three marks
# and print  the name of the student who got the highest total among them.

# Print "No student found" if there are no students how have
# score more than 90 in all 3 subjects. 

# For example:

# Test	Result
# highest_marks(["jason", "priya", "madhan", "syed"], 
#               [91, 92, 81, 75],
#               [91, 89, 100, 90],
#               [91, 95, 100, 90])

def highest_marks(names,maths,physics,chemistry):
    name1=[]
    math=[]
    phy=[]
    chem=[]
    for i in range(len(names)):
        if maths[i]>=90 and physics[i] >=90 and chemistry[i]>=90:
            name1.append(names[i])
            math.append(maths[i])
            phy.append(physics[i])
            chem.append(chemistry[i])
    if len(name1)==0:
        print("No students found")
        return
    else:
        max_name=name1[0]
        max_sum=math[0]+phy[0]+chem[0]
        for i in range(1,len(name1)):
            sum=math[i]+phy[i]+chem[i]
            if sum>max_sum:
                max_name=name1[i]
                max_sum=sum
        print(max_name) 

highest_marks(["jason", "priya", "madhan", "syed"], 
              [91, 92, 81, 75],
              [91, 89, 100, 90],
              [91, 95, 100, 90])
highest_marks(["Ameer", "Bobby", "Clara", "Divya", "Elvin", "Fazil", "Geeta", "Hari", "Ila", "Jay"],
[85, 88, 89, 90, 86, 87, 84, 83, 89, 88],
[84, 87, 88, 89, 85, 86, 83, 82, 88, 87],
[86, 85, 84, 83, 87, 88, 82, 81, 85, 86])
        
        


        
   
    
    
           
            

            
            
    

        



    

        