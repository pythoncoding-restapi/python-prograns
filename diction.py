#dictionary
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is : ", capitals['Gujarat'])
print ("Capital of Karnataka is : ", capitals['Karnataka'])
#Using the get() Method
#val = dict.get("key")
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is: ", capitals.get('Gujarat'))
print ("Capital of Karnataka is: ", capitals.get('Karnataka'))
#get() method accepts an optional string argument. If it is given, and if the key is not found, this string becomes the return value.
#get() method doesn't raise error if the key is not found; it return None.
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Haryana is : ", capitals.get('Haryana', 'Not found'))
#Empty Dictionary
d1 = dict()
d2 = {}
print ('d1: ', d1)
print ('d2: ', d2)
#Dictionary from List of Tuples
# list or tuple of two-item tuples. First item as key, and  second as its value.

d1=dict([('a', 100), ('b', 200)])
d2 = dict((('a', 'one'), ('b', 'two')))
print ('d1: ', d1)
print ('d2: ', d2)
#[]" operator (used to access value mapped to a dictionary key) is used to update an existing key-value pair as well as add a new pair.

#Syntax dict["key"] = val
#If the key is already present in the dictionary object, its value will be updated to val. If the key is not present in the dictionary, a new key-value pair will be added.

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: ", marks)
marks['Laxman'] = 95
print ("marks dictionary after update: ", marks)
#Using the Union Operator (|)
#Python introduces the "|" (pipe symbol)

d3 = d1 | d2
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = marks | marks1
print ("marks dictionary after update: \n", newmarks)
#Using del Keyword
#Python's del keyword deletes any object from the memory. Here we use it to delete a key-value pair in a dictionary.
#del dict['key']

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before delete operation: \n", numbers)
del numbers[20]
print ("numbers dictionary before delete operation: \n", numbers)
#Using pop() Method
# pop() method of dict class causes an element with the specified key to be removed from the dictionary.

#Syntax val = dict.pop(key)
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before pop operation: \n", numbers)
val = numbers.pop(20)
print ("nubvers dictionary after pop operation: \n", numbers)
print ("Value popped: ", val)
#Using clear() Method
#The clear() method in dict class removes all the elements from the dictionary object and returns an empty object.
#Syntax dict.clear()
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before clear method: \n", numbers)
numbers.clear()
print ("numbers dictionary after clear method: \n", numbers)
# simple for loop over the dictionary object traverses the keys used in it.

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x)

