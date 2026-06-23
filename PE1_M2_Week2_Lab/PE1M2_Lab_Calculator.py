###################################################
# Name: Crystal Edwards-Flores                    #
# Course: CWCT-140                                #
# Date: June 17, 2026                             #
# Program: PE1M2_Lab_Calculator.py                #
# Description: Implement Python Calculator        #      
###################################################

from inspect import Parameter


print("Welcome to the Python Calculator")
print("This program will add, subtract, multiply, and divide two numbers")
print("Input the expression in form \"x <op> y\", e.g. 73 * 88")

calmessage = input("Expression: ")

parameters = calmessage.split()
value1 = float(parameters[0])
operator = parameters[1]
value2 = float(parameters[2])

if operator == "+":
    result = value1 + value2
elif operator == "-":
    result = value1 - value2
elif operator == "*":
    result = value1 * value2
elif operator == "/":
    result = value1 / value2

print("%-4.2f\t%1s\t%-4.2f = %-8.2f"%(value1, operator, value2, result))