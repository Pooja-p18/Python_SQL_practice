s = {"apple", "banana", "cherry"}
print(s)

#duplicates are not allowed
s = {"apple", "banana", "cherry", "apple"}
print(s)

s = {"apple", "cherry", True, False, 0, 1}
print(s)
print(len(s))


s1= {"apple", "banana", "cherry"}
s2= {1,5,7,9,3}
s3= {True,False,False}
print(s1, s2, s3)

set1 = {"abc", 34, True, 40, "male"}
print(set1)

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry"))
print(thisset)

#access set items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("kiwi" not in thisset)

s = {"apple", "banana", "cherry"}
s.add("orange")
print(s)

s = {"apple", "banana", "cherry"}
t = {"pineapple", "mango", "papaya"}
s.update(t)
print(s)

set = {"apple", "banana", "cherry"}
list = ["kiwi", "orange"]
set.update(list)
print(set)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Remove items
thisset = {"apple", "banana", "cherr"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

t = {"apple", "banana", "cherry"}
x = t.pop()
print(x)
print(t)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#thisset = {"apple", "banana", "cherry"}
#del thisset
#print(thisset)

#loop sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
#Join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)


x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

set1 = {"a", "b", "c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)