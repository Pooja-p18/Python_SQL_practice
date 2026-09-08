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

