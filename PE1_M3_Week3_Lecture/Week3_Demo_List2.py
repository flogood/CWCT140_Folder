myList = [1, 2, 3, 4, 5, "a", "b", "c", True, False]
         #0  1  2  3  4   5    6    7   8    9
         #-10 -9 -8 -7 -6  -5   -4   -3  -2  -1


myList2 = [1, 2, 3]

myList2.append(4)
print(myList2)

myList2.append(5)
print(myList2)

myList2.insert(0, -1)   #[-1, 1, 2, 3, 4, 5]
print(myList2)

myList2.insert(2, -1)   #[-1, 1, -1, 2, 3, 4, 5]
print(myList2)

myList2.insert(len(myList2)-1, -1)
print(myList2)

del myList2[0]
print(myList2)   #[1, -1, 2, 3, 4, -1, 5]

del myList2[0:3:2]   #[-1, 3, 4, -1, 5]
print(myList2)


myList2.reverse()
print(myList2)

myList2.remove(-1)
print(myList2)