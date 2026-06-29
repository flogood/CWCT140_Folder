################################
# Program name: PE1_M3_Lab.py
#  Author: Crystal Edwards-Flores
#  Course: Python Essentials 1
#  Date: 6/272026
#  Assignment: Module 3 - Bubble sort
#  Purpose: Bubble Sort with bar graph
########################################


# Function to plot bar grapghs
def plotBars(data_list, plotsymbol):

    for i in range(len(data_list)):
        print()

    for value in data_list:
        print(plotsymbol * value)

        print()

def bubbleSort(sorted_list):
    for outer_index in range(len(sorted_list)):
        # call plotBars subroutine
        plotBars(sorted_list, '*')
        for inner_index in range(0, len(sorted_list) - outer_index - 1):
            if sorted_list[inner_index] > sorted_list[inner_index + 1]:
                temp = sorted_list[inner_index]
                sorted_list[inner_index] = sorted_list[inner_index + 1]
                sorted_list[inner_index + 1] = temp
    
    # call plotBars subroutine
    plotBars(sorted_list, '*')

#Main program
# Build a list of numbers between 1 and 50
theList = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

plotBars(theList, '*')
print("The data is:", theList)
print()

theList.reverse()
plotBars(theList, '*')
print("The reversed data is:", theList)
print()

print("The following is bubble sort results:")
bubbleSort(theList)
