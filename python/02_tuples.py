thistuple = ("apple", "banana", "cherry")
print(thistuple)

#allows duplicates
thistuple = "apple", "banana", "cherry", "banana", "apple"
print(thistuple)
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))                   

#empty tuple
thistuple = ()
print(type(thistuple))   

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1,5,7,9,3,4,6)
tuple3 = (True, False, False)  
print(tuple1, tuple2, tuple3)  

tuple1 = ("abc", 34, True, 40, "male")           
print(tuple1)

thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)

#Access Tuples
t = ("apple", "banana", "cherry")
print(t[1])
print(t[-1])

t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t[2:5])
print(t[:4])
print(t[2:])
print(t[-4:-1])
if "apple" in t:
    print("Yes its there")
    
#Update tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)

#add tuple to tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#remove
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(y)

t = ("apple", "banana", "cherry")
del thistuple
print(t)

#unpack tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#loop lists
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
    
#loop through the index numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
    

t = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
    
#join tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits= ("apple", "kiwi", "orange")
mytuple= fruits*2
print(mytuple)

