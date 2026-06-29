################################
# Program name: PE1_M3_Triangle.py
#  Author: Crystal Edwards-Flores
#  Course: Python Essentials 1
#  Date: 6/24/2026
#  Assignment: Module 3 - Triangle
#  Purpose: Determine triangle based on lengths
########################################

inputString = input("type in three triangle lengths (spererated by spaces): ")

value = inputString.split()

try:
    a = float(value[0])
    b = float(value[1])
    c = float(value[2])
except ValueError:
    print("You did not input three numerical numbers.")
    exit()
except IndexError:
    print("You did not type in three numbers or separate them by a space")
    exit()
except:
    print("Your input is not valid.")
    exit()


if a <= 0 or b <= 0 or c <= 0:
    print("Edge length cannot be zero or negative value.")
    exit()

#First determine if three lengths can form a triangle
if a + b > c and a + c > b and b + c > a:
    print("Three edge lengths can form a triangle.")

    if a==b or b==c or a==c:
        print("Three edge lengths can form an isosceles triangle.")

    if a==b and b==c:
        print("Three edge lengths can form an equilateral triangle.")
    elif a**a + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Three edge lengths can form a right triangle.")               
            
    else:
        if a**2 + b**2 == c**2 or c**2 == b**2 or b**2 + c**2 == a**2:
            print("Three edge lengths can form a right triangle.")

else:
    print("Three edge lengths cannot form a triangle")

