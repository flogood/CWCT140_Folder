myList = [1, 2, 3, 4, 5]

myShallowList = myList

print(myList)
print(myShallowList)

del myShallowList[0]

print(myList)
print(myShallowList)

myList.insert(0, 10)

print(myList)
print(myShallowList)