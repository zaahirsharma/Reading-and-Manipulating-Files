
Input1 = []
Input2 = []
Output = []
fileID = open("test_data.csv",'r')
LineI = fileID.readline()

while LineI !="":
    LineI = fileID.readline()
    if LineI !="":
        Values = LineI.rstrip('\n').split(',')
        try:
            Input1.append(float(Values[0]))
        except ValueError:
            continue
        try:
            Input2.append(float(Values[1]))
        except ValueError:
            continue
        try:
            Output.append(float(Values[2]))
        except ValueError:
            continue
fileID.close()
# print('-------------------------------------------------')
# print("Input1 = ", Input1)
# print('-------------------------------------------------')
# print("Input2 = ", Input2)
# print('-------------------------------------------------')
# print("Output = ", Output)    
# print('-------------------------------------------------')




# The problem: Given measurements from sensors Input1, Input2 & Output the written function implement the logic as mentioned below
# This is a custom function that takes in ONE Value from Input1 (x1) and Input2(x2) and returns ONE output --> My_Output
# Also it passes a TOLERANCE as an additional argument into the function. e.g. My_Output(x1,x2,TOL)
# All arguments required by the function are passed in as arguments and My_Output value is returned

###################   This is the logic the function uses for production:##################################

# 1. if x1 is less than x2 then return 'cosine' of 'x1'
# 2. if x1 is equal to x2 then return 1 (MUST COMPARE floating point numbers within TOL = 10**-6)
# 3. if x1 is greater than x2 then return 'sine' of 'x2'. 
# trignometric functions are in the math library



from math import *

def My_Output(num1, num2, TOL):
    if num1 < num2:
        return cos(num1)
    elif num1 > num2:
        return sin(num2)
    elif num1 == num2:
        if abs(num1-num2) < TOL:
            return 1

    

 

###################   This is the logic the function uses for production for this section :##################################

# 1. Passes one pair (row) of x1, x2 value & TOLERANCE to the above defined function and compares My_Output to the corresponding values in Output provided in file.
# 2. This occurs for all inputs (every row of file provided) - in a loop
# 3. It also prints to console number of successes (My_Output matches given Output to specified TOLERANCE)
# 4. Prints to console number of failures
# 5. Prints 'percentage of total successes' = [successes/(successes+failures)]*100 to console. This is the approx score.

        
tolerance = 10**-6
success_num = 0
success_percent = 0
failure_num = 0
for i in range(len(Input1)):
    result = Your_Output(Input1[i],Input2[i],tolerance)
    if (result-Output[i]) < tolerance:
        success_num += 1
    else:
        failure_num += 1
        print(i)
        
success_percent = (success_num/(success_num+failure_num))*100

print(success_num,failure_num,f"{success_percent}%")



# This part uses matplotlib 
# Produces two overplotted plots  
# 1. Plots Points and LINE through them between 'Input1' (X-Axis) versus 'My_Output' (Y-Axis) in BLUE
# 2. Over Plot a RED line with Points between 'Input2' (X-Axis) versus ' My_Output' (Y-Axis) 

import matplotlib.pyplot as plt

plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.title("Comparing Results Rrom Input1 and Input2 to Your_Output'")
output = []
for j in range(len(Input1)):
    output.append(Your_Output(Input1[j], Input2[j], 10**-6))
for i in range(len(Input1)):
    plt.scatter(Input1[i],Your_Output(Input1[i], Input2[i], 10**-6), c = 'b', marker = 'o') 
    plt.scatter(Input2[i],Your_Output(Input1[i], Input2[i], 10**-6), c = 'r', marker = 'o')
plt.plot(Input1,output, '.b-')
plt.plot(Input2,output, '.r-')
plt.show()



    
    
