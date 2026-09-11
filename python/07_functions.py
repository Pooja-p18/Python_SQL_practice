def my_function():
    print("Hello from a function")
    
my_function()
my_function()
my_function()

def f_to_c(temp):
    return (temp - 32) * 5 / 9
print(f_to_c(77))
print(f_to_c(95))
print(f_to_c(50))

def greet():
    return "Hello from a function"
message = greet()
print(message)
print(greet())

def my_function():
  pass

def my_func(fname):
    print(fname + " Refsnes")
my_func("Emil")
my_func("Tobias")
my_func("Linus")

def my_func(name):
    print("Hello", name)
my_func("Emil")

def my_func(fname, lname):
    print(fname + " " + lname)
my_func("Emil", "Refsnes")

def my_function(name = "friend"):
  print("Hello", name)
my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

def my_function(country = "Norway"):
  print("I am from", country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_func(animal, name):
    print("I have a", name)
    print("My", animal + "'s name is", name)
my_func(animal= "dog", name= "Buddy") 

#positional arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function("dog", "Buddy")
my_function("Buddy", "dog")

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)
my_function("dog", name = "Buddy", age = 5)

def my_func(fruits):
    for fruit in fruits:
        print(fruit) 
my_fruits = ["apple", "banana", "cherry"]
my_func(my_fruits) 

def my_func(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
my_person = {"name": "Emil", "age": 25}
my_func(my_person)

def my_func(x, y):
    return x + y
result = my_func(5, 3)
print(result)

def my_func():
    return ["apple", "banana", "cherry"]
fruits = my_func()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_func():
     return (10, 20)
x, y = my_func()
print("x:", x)
print("y:", y)

def my_func(name, /):
    print("Hello", name)
my_func("Emil")

def my_function(name):
  print("Hello", name)
my_function(name = "Emil")

def my_func(*, name):
    print("Hello", name)
my_func(name = "Emil")

def my_function(a, b, /, *, c, d):
  return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_func(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)
my_func("Emil", "Tobias", "Linus")

def my_func(greeting, *names):
    for name in names:
        print(greeting, name)
my_func("Hello", "Emil", "Tobias", "Linus")

def my_func(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_func(1, 2, 3))
print(my_func(10, 20, 30, 40))
print(my_func(5))
        
def my_func(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(my_func(3, 7, 2, 9, 1))
    
def my_func(**kid):
    print("His last name is " + kid["lname"])
my_func(fname = "Tobias", lname = "Refsnes")

def my_func(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)
my_func(name = "Tobias", age = 30, city = "Bergen")

def my_func(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)
my_func("email23", age = 25, city = "Oslo", hobby = "Coding")

def my_func(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
my_func("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

def my_func(a, b, c):
    return a + b + c
numbers = [1, 2, 3]
result = my_func(*numbers)
print(result)

def my_function(fname, lname):
  print("Hello", fname, lname)
person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) 

#Python scope
def myfunc():
    x = 300
    print(x)
myfunc()

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

x = 300
def myfunc():
    print(x)
myfunc()
print(x)

x = 300
def myfunc():
    x = 200
    print(x)
myfunc()
print(x)

def myfunc():
    global x
    x = 300
myfunc()
print(x)

x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)

x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()
print("Global:", x)

#Lambda functions
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))  

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x : x * 2, numbers))
print(doubled)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x : x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x : len(x))
print(sorted_words)

#Recursion
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)
countdown(5)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_of_rest = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest
my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))
    