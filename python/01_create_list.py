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

#Looping Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
 
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
     print(thislist[i])
    
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
    
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
        if "a" in x:
            newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "kiwi"]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in range(10)]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#Sorting lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

x = [100,50,20,67,23,82]
x.sort()
print(x)

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort(reverse = True)
print(fruits)

x = [100,50,20,67,23,82]
x.sort(reverse = True)
print(x)

#customizing sort function
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

#case insenitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#case insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copying a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#list method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Using slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
              

#Joining lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Appending
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

#extend method
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
