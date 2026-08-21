thislist = ["apple","banana","cherry","mango","kiwi","orange"]
print(thislist)
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(type(list1))
print(type(list2))
print(type(list3))

thislist = list(("apple", "banana", "kiwi", "cherry"))
print(thislist)


#Accessing the list items
thislist = ["apple", "banana", "cherry","mango", "kiwi", "orange"]
print(thislist[3])

#negative indexing
thislist = ["apple", "banana", "cherry","mango", "kiwi", "orange"]
print(thislist[-2])

#ranges of indexes
thislist = ["apple", "banana", "cherry","mango", "kiwi", "orange"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry","mango", "kiwi", "orange"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry","mango", "kiwi", "orange"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry","mango", "kiwi", "orange"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry","mango", "kiwi", "orange"]
if "papaya" in thislist:
    print("Yes, 'papaya' is in the fruits list")
else:
    print("No, 'papaya' is not in the fruits list")
    
    
# -------------------------
# Changing List Items
# -------------------------
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Add list items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove list items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)