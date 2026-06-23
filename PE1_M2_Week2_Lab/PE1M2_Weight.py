###################################################
# Name: Crystal Edwards-Flores                    #
# Course: CWCT-140                                #
# Date: June 17, 2026                             #
# Program: PE1M2_Weight.py                        #
# Description: Calculate weight on other planets  #      
###################################################

planetlist = ["Sun", "Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
gravitylist = [27.01, 0.38, 0.91, 1.00, 0.17, 0.38, 2.34, 1.06, 0.92, 1.19, 0.06]

#Ask user to type in their name
name = input("Please type your name: ")

#Ask user to type in their weight
try:
    weight = float(input("Please type your weight(in pounds): "))
except:
    print("You did not type in a number")
    exit()
else:
    if weight <= 0:
        print("You typed in a negative number")
        exit()

print("Hello", name, "Welcome to the Solar system.")

for i in range(len(planetlist)):
    print("{:<30s}{:>7.2f}{:<8s}".format("Your weight on " + planetlist[i] + " is", weight*gravitylist[i], "pounds"))
