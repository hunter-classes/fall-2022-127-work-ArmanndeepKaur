#Exercise 3 

myList = [76, 92.3, "hello", True, 4, 76]
#a
myList.append("apple")
myList.append(76)
#b
myList.insert(3, "cat")
#c
myList.insert(0, 99)
#d
print(myList.index("hello"))
#e
print(myList.count(76))
#f
myList.remove(76)
#g
#myList.pop(True) --> doesn't work
#myList.index(True) --> doesn't work
myList.pop(myList.index(True))

print(myList)