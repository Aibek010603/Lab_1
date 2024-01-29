#syntax ex1
print("Hello,world")


#syntax ex2
if 5 > 2:
 print ("YES")
 
 
 #comments ex1
 #This is a comment
 
 
 #comments ex2
 """"
 This is a coment
 written in
 more than just one line
 """
 
 
 #Variables ex1
 carname = "Volvo"
 
 
 #Variablex ex2
 x = 50
 
 
 #Variables ex3
 x = 5
 y = 10
 print (x + y)
 
 
 #Variables ex4
 x = 5
 y = 10
 z = x + y
 print(z)
 
 
 #Variables ex5
 x, y, z = "Orange", "Banana", "Cherry"
 
 
 #Variables ex6
 x = y = z = "Orange"
 
 
 #Variables ex7
 def myfunc():
     global x
     x = "fantastic"
     
     
#Data Types ex1    
x = 5
print(type(x))
int


#Data Types ex2
x = "Hello, World"
print(type(x))
str


#Data Types ex3
x = 20.5
print(type(x))
float


#Data Types ex4
x = ["banana", "apple", "cherry"]
print(type(x))
list


#Data types ex5
x = ("apple", "banana", "cherry")
print(type(x))
tuple


#Data types ex6
x = {"name" : "John", "age" : 36}
print(type(x))
dict


#Data types ex7
x = True
print(type(x))
bool


#Numbers ex1
x = 5
x = float(x)


#Numbers ex2
x = 5.5
x = int(x)


#Numbers ex3
x = 5
x = complex(x)


#Strings ex1
x = "Hello,World"
print(len(x))


#Strings ex2
txt = "Hello,World"
x = (txt[0])


#Strings ex3
txt = "Hello,World"
x = (txt[2:5])


#Strings ex4
txt = "Hello,World"
x = txt.strip()


#Strings ex5
txt = "Hello,World"
x = txt.upper()


#Strings ex6
txt = "Hello,World"
x = txt.lower()


#Strings ex7
txt = "Hello,World"
x = txt.replace("H", "J")


#Strings ex8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

