'''
This is the template file for the In Class Coding Exam - Fill in your Name, Section & Date below
Name: ZAAHIR SHARMA
Sec #: 551
Date:  NOVEMBER 27, 2023
    
Aggie Code of Honor:
By uploading this file to Canvas, I pledge that I have neither given nor received aid in completing this exam. 
In addition, I have followed the strictures of the Texas A&M University Aggie Honor Code during today's test period.
'''



'''############ Instructions for FINAL Coding Exam ###############################

Scenario: After Freshman Year, you are given an Internship to automate some 
computations as part of a larger group. You are to provide your solution using
the Python language. 

You are provided a template file pre-named Custom_Script.py. You should use 
THIS file so that all code by other interns can be integrated into one complete
package. Hence, you must stick to the format dictated by the template. 

You are given a sample test file test_data.csv to help you validate your code,
but your evaluation will be based on a larger test data set that you do not
have access to. It should be your intent to make sure your script will handle
all possible test cases as per the specifications below.

The python file you submit must have the name Custom_Script.py as provided.
This file provided as a template comes along with stub code to read test_data.csv 
and provide variables Input1, Input2 & Output for checking your code. 
DO NOT CHANGE THESE NAMES. 

MAKE SURE YOU PUT BOTH FILES Custom_Script.py & test_data.csv IN SAME FOLDER

Read each section below and complete the code as requested. '''


'''PART A.	Section of Custom_Script.py: 
------ File Read Template Provided ---- YOU DO NOT HAVE ANY CODE TO WRITE HERE

# # Run to see Input & Output in "Variable Explorer" before you code next sections
# # First clear all other variables in your memory
# # Reads test_data.csv and CONVERTs to Float VARIABLEs in LISTs: Input1, Input2 & Output
'''

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


''' ------------------------ YOUR SOLUTION BELOW THIS LINE ---------------------------

# # Part B Section of Custom_Script.py: [30%] – Writing functions & Coding Conditional Logic

# The problem: Given measurements from sensors Input1, Input2 & Output you must write a function that implements the logic as mentioned below
# Write your custom function that takes in ONE Value from Input1 (x1) and Input2(x2) and returns ONE output --> Your_Output
# Also pass in TOLERANCE as an additional argument into the function. e.g. Your_Function(x1,x2,TOL)
# Ensure all arguments required by the function are passed in as arguments and Your_Output value is returned
# If Your_Output matches the test data Output provided, you know your function is working correctly. 
# Else debug and fix your code before proceeding.

###################   This is the logic your function has to produce:##################################

1. if x1 is less than x2 then return 'cosine' of 'x1'
2. if x1 is equal to x2 then return 1 (MUST COMPARE floating point numbers within TOL = 10**-6)
3. if x1 is greater than x2 then return 'sine' of 'x2'. 
trignometric functions are in the math library

###########   RUBRIC   ###########
Function definition --> 10 points - Ensure all arguments requested by the function are passed in as arguments e.g. Your_Function(x1,x2,TOL)
Conditional logic   --> 10 points [3 Points for < & > conditions, and 4 Points for equality with TOLERANCE]
Return Values       --> 10 points
'''

from math import *

def Your_Output(num1, num2, TOL):
    if num1 < num2:
        return cos(num1)
    elif num1 > num2:
        return sin(num2)
    elif num1 == num2:
        if abs(num1-num2) < TOL:
            return 1

    

'''  Part C. Section of Custom_Script.py: [30%] – Calling your Function in a Loop & Testing your_output for all inputs provided
# Ensure you are comparing floating point numbers using a tolerance of 10**-6. 
# Ensure you can test against the length of data rows of the Input array. 
# We will use a test file with different number of rows (than currently provided) to test your solution and your code should still work. 
# You can assume Input and Output are lists (arrays) of the same length. 
# These list variables are floating point numbers and row values correspond to each other. 

###################   This is the logic this section of your code has to produce:##################################
1. Pass one pair (row) of x1, x2 value & TOLERANCE to YOUR above defined function and compare Your_Output to the corresponding values in Output provided in file.
    Note: Ensure you are comparing floating point numbers using a tolerance specified. 
2. Do this for all inputs (every row of file provided) - in a loop
3. If your function output matches the output given in file you have success. (Compare floating point numbers with Tolerance specified)
4. Print to console number of successes (Your_Output matches given Output to specified TOLERANCE)
5. Print to console number of failures
6. Print 'percentage of total successes' = [successes/(successes+failures)]*100 to console. ######  This is your approximate score. #####

###########   RUBRIC   ###########
Proper Loop structure              --> 10 points
Compute Success/Failures           --> 10 points (using TOL 10**-6)
Print Values (Success/Failures/%)  --> 10 points
'''
        

        
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




''' Part D. Section of Custom_Script.py: [30%] – Testing Plots

# Use matplotlib 
# Produce two overplotted plots  
# 1. Plot Points and LINE through them between 'Input1' (X-Axis) versus 'Your_Output' (Y-Axis) in BLUE
# 2. Over Plot a RED line with Points between 'Input2' (X-Axis) versus ' Your Output' (Y-Axis) 
 
# # Label both your plot with appropriate X-Axis, Y-Axis Labels and title.
Example Plot is provided for verification "Figure.png"

###########   RUBRIC   ###########
Plot1          --> 10 points (Blue Points)
Plot2          --> 10 points (Red Line)
Figure Title  --> 2 points
X & Y Labels  --> 8 points
'''

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



''' Part E. Enter your grade (Success= yourScore%) to Canvas in the Text Box 

###########   RUBRIC   ###########        
Score entry ---> [10 Points]


UPLOAD ONLY YOUR Solution Custom_Script.py to Canvas. NOT THE DATA FILE
# Make sure to upload correct file. We cannot grade if you upload the wrong file.
 

'''
    
    