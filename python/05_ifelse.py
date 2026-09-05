a = 33
b = 200
if b > a:
    print("b is greater than a")
    
n = 15
if n > 0:
    print("The number is positive")

#multiple statements in a block
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
  
#using variable in condition
is_logged_in = True
if is_logged_in:
    print("Welcome back!")
    
a = 20
b = 20
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
    
score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
    
age = 25
if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")
  
#Day of the week checker:
day = 3
if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")
  
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
    
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
number = 7
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
    
temperature = 22
if temperature > 30:
    print("Its hot outside!")
elif temperature > 20:
    print("Its warm outside")
elif temperature > 10:
    print("Its cool outside")
else:
    print("Its cold outside!")
    
    
username = "Emil"
if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
  
#shorthand If
a = 5
b = 2
if a > b:
    print("a is greater than b")
    
a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")