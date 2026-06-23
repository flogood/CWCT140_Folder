#################################################
# Name: Crystal Edwards-Flores                  #
# Course: CWCT-140                              #
# Date: June 17, 2026                           #
# Program: PE1M2_RestaurantBill.py              #
# Description: Calculate resturant bill         #      
#################################################

taxRate = 0.0675
suggestedTipRate = 0.18

try:
    mealCost = float(input("Please type meal cost: $"))
except:
    print("You did not type in a dollar amount")
    exit()
else:
    if mealCost <= 0:
        print("You typed in a negative dollar amount")
        exit()


tax = mealCost*taxRate
suggestedTip = (mealCost+tax)*suggestedTipRate
print("Suggested tip amount: $%-6.2f"%(suggestedTip))

try:
    actualTip = float(input("Please type the tip amount: $"))
except:
    print("You did not type the correct dollar amount")
    exit()
else:
    if mealCost <= 0:
        print("You did not type in a dollar amount")
        exit()

totalBill = mealCost + tax + actualTip

print("Meal amount is $", mealCost)
print("Tax amount is $", tax)
print("Tip amount is $", actualTip)
print("Total bill is $", totalBill)