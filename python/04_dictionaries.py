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

