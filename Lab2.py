#Booleans ex1
print(10 > 9)
True
#Booleans ex2
print(10 == 9)
False
#Booleans ex3
print(10<9)
False
#Booleans ex4
print(bool("abc"))
True
#Booleans ex5
print(bool(0))
False
#Operators ex1
print(10 * 5)
#Operators ex2
print(10 / 2)
#Operators ex3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")
#Operators ex4   
if 5 != 10:
    print("5 and 10 is not equal")
#Opearators ex5   
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")
#List ex1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#List ex2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#List ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#List ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#List ex5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#List ex6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#List ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#List ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
#Tuples ex1
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
#Tuples ex2
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
#Tuples ex3
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#Tuples ex4
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#Sets ex1
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Yes, apple is a fruit")
#Sets ex2   
fruits = ["apple", "banana", "cherry"]
fruits.add("orange")
#Sets ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#Sets ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#Sets ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
#Dictionaries ex1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#Dictionaries ex2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
#Dictionaries ex3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
#Dictionaries ex4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#Dictionaries ex5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
#If...Else ex1
a = 50
b = 10
if a > b:
    print("Hello World") 
#If...Else ex2
a = 50
b = 10
if a != b:
    print("Hello World")
#If...Else ex3
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")
#If.Else ex4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
#If...Else ex5
if a == b and c == d:
    print("Hello")    
#If...Else ex6
if a == b or c == d:
    print("Hello")  
#If...Else ex6
a=12
b=13
c=14
d=14
if a == b or c == d:
    print("hello")
#If...Else ex7
if 5 > 2:
    print("yes")
#If...Else ex8
a = 2
b = 5
print("yes") if a == b else print("no")
#If...Else ex9
a = 2
b = 50
c = 2
if a == c or b == c :
    print("yes")
#While Loops ex1
i=1
while i<6:
    print(i)
    i += 1
#While Loops ex2
i = 1
while i < 6:
    if i == 3:
        break
    i +=1
#While Loops ex3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
#While Loops ex4
i = 1
while i < 6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")
#For Loops ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#For Loops ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
#For Loops ex3
for x in range(6):
  print(x)
#For Loops ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
print(x)
