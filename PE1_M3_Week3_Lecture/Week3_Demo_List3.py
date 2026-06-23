myList = [1, 2, 3, 4, 5]

myDeepCopyList = myList[1:3]

print(myList)
print(myDeepCopyList)

del myDeepCopyList[0]

print(myList)
print(myDeepCopyList)

myList.insert(0, 10)

print(myList)
print(myDeepCopyList)


""""
myShallowList = myList

print(myList)
print(myShallowList)

del myShallowList[0]

print(myList)
print(myShallowList)

myList.insert(0, 10)

print(myList)
print(myShallowList)
"""