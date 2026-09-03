t = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(t)
print(t["model"])

#duplicates are not allowed
t = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2000
}
print(t)
print(len(t))

t = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(t)
print(type(t))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#accessing items
t = {
    "brand" : "Honda",
    "model" : "SUV",
    "year" : 1986
}
x = t["model"]
print(x)
x = t.get("year")
print(x)

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = car.keys()
print(x)
car["color"] = "white"
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x)
car["year"] = 2020
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x)
car["color"] = "Red"
print(x)
if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary")
    
#Change 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({'year':2020})  #using update
print(thisdict)

#Adding items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)

#REMOVING
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#LOOP Dictonaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)
for x in thisdict:
    print(thisdict[x])
for x in thisdict.keys():
    print(x)
for x in thisdict.values():
  print(x)
for x, y in thisdict.items():
  print(x, y)
  
#COPY Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#NESTED Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
print(myfamily["child2"]["name"])
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])