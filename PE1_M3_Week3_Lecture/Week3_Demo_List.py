myList = [1, 2, 3, 4, 5, "a", "b", "c", True, False]
         #0  1  2  3  4   5    6    7   8    9
         #-10 -9 -8 -7 -6  -5   -4   -3  -2  -1

print(len(myList))
print(myList)

print(myList[0], myList[-10])
print(myList[9], myList[-1])

i = 4

print(myList[i], myList[-len(myList) + i])

# :  range operator

print(myList[:])
print(myList[0:10])     #0.....9
print(myList[3:10])     #3.....9
print(myList[0:10:2])   #0,2,4,6,8

#print(myList[-5:2])   #0,3,6,9
print(myList[-5:-2])  

print(myList[-8:8])    #0,2,4,6,8