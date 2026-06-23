###################################################
# Name: Crystal Edwards-Flores                    #
# Course: CWCT-140                                #
# Date: June 17, 2026                             #
# Program: PE1M2_Lab_Calculator.py                #
# Description: Implement Python Calculator        #      
###################################################

print("Welcome to the Python Calculator")
print("This program will add, subtract, multiply, and divide two numbers")
print("Input the expression in form \"x <op> y\", e.g. 73 * 88")

calmessage = input("Expression: ")

parameters = calmessage.split()

if len(parameters) != 3:
    print("You did not type in expression in the correct format")
    exit()

value1 = float(parameters[0])

operator = parameters[1]

value2 = float(parameters[2])

match operator:
    case "+":
        result = value1 + value2
    case "-":
        result = value1 - value2
    case "*":
        result = value1 * value2
    case "/":
        result = value1 / value2
    case _:
        print("Invalid operator, cannot calculate")
        exit()
        
print("%-4.2f\t%1s\t%-4.2f = %-8.2f"%(value1, operator, value2, result))