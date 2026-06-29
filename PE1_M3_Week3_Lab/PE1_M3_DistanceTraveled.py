################################
# Program name: PE1_M3_DistanceTraveled.py
#  Author: Crystal Edwards-Flores
#  Course: Python Essentials 1
#  Date: 6/272026
#  Assignment: Module 3 - Distance Traveled
#  Purpose: Calculate distance traveled
########################################


inputSpeed = input("What is the speed of the vehicle in mph? ")
inputHours = input("How many hours has it traveled? ")

try:
    speed = int(inputSpeed)
    hours = int(inputHours)
except:
    print("You did not type in interger values for speed and hours.")
    exit()

if speed < 0 or hours < 1:
    print("The speed should not be negative or time traveled should be greater or equal to 1.")
    exit()

print()
print("Hour  Distance  Traveled")
print("-------------------------")

for h in range(1, hours + 1):
    print("%-6d%d"%(h, h*speed))