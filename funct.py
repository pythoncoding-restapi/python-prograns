#Example
# name variable inside the function.

def greetings(name):
   "This is docstring of greetings function"
   print ("Hello {}".format(name))
   return
   
greetings("Samay")
greetings("Pratima")
greetings("Steven")
#Positional Arguments Example
def add(x,y):
   z=x+y
   print ("x={} y={} x+y={}".format(x,y,z))

a=10
b=20
add(a,b)
#Arbitrary Arguments Example
#Given below is an example of arbitrary or variable length positional arguments −


def add(*args):
   s=0
   for x in args:
      s=s+x
   return s
result = add(10,20,30,40)
print (result)

result = add(1,2,3)
print (result)
#Arbitrary Keyword Arguments (**kwargs)
def addr(**kwargs):
   for k,v in kwargs.items():
      print ("{}:{}".format(k,v))

print ("pass two keyword args")
addr(Name="John", City="Mumbai")
print ("pass four keyword args")

# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")
# Example of Default Arguments
# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )
#Example: Calling Function Without Keyword Arguments

def percent(phy, maths, maxmarks=200):
   val = (phy+maths)*100/maxmarks
   return val

phy = 60
maths = 70
result = percent(phy,maths)
print ("percentage:", result)

phy = 40
maths = 46
result = percent(phy,maths, 100)
print ("percentage:", result)
#Example of Keyword Arguments
# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
# by positional arguments
printinfo ("Naveen", 29)

# by keyword arguments
printinfo(name="miki", age = 30)
#Arbitrary Arguments Example
#Given below is an example of arbitrary or variable length positional arguments −

# sum of numbers
def add(*args):
   s=0
   for x in args:
      s=s+x
   return s
result = add(10,20,30,40)
print (result)

result = add(1,2,3)
print (result)
#example of keyword arguments
def addr(**kwargs):
   for k,v in kwargs.items():
      print ("{}:{}".format(k,v))

print ("pass two keyword args")
addr(Name="John", City="Mumbai")
print ("pass four keyword args")

# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")
