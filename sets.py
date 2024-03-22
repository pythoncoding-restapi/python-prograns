#Duplicate values will be ignored:

set= {"pen", "pencil", "crayon", "eraser"}

print(set)
#True and 1 is considered the same value:

set= {"pen", "pencil", "crayon", "eraser",True, 1, 2}

print(set)
#False and 0 is considered the same value:

set= {"pen", "pencil", "crayon", "eraser",True, False, 0}

print(set)
print(len(set))
# set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}
#Access Set Items in loops

langs = {"C", "C++", "Java", "Python"}
for lang in langs:
   print (lang)
#Check Set Item Exists
langs = {"C", "C++", "Java", "Python"}
print ("PHP" in langs)
print ("Java" in langs)
#Add Set Items
#The add() method in set class adds a new element. If the element is already present in the set, there is no change in the set.

lang1 = {"C", "C++", "Java", "Python"}
lang1.add("Golang")
print (lang1)
#Add Sets Using update() Method
lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang1.update(lang2)
print (lang1)
#Combine Unique Set Items

lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang3 = lang1.union(lang2)
print (lang3)
#Remove Set Items
lang1 = {"C", "C++", "Java", "Python"}
print ("Set before removing: ", lang1)
lang1.remove("Java")
print ("Set after removing: ", lang1)
lang1.remove("PHP")
#pop method to remove items in set
lang1 = {"C", "C++"}
print ("Set before popping: ", lang1)
obj = lang1.pop()
print ("object popped: ", obj)
print ("Set after popping: ", lang1)
obj = lang1.pop()
obj = lang1.pop()
#Remove All Set Items using clear() method
lang1 = {"C", "C++", "Java", "Python"}
print (lang1)
print ("After clear() method")
lang1.clear()
print (lang1)
#Remove Items that Exist in Both Sets by difference_update() method 
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1 before running difference_update: ", s1)
s1.difference_update(s2)
print ("s1 after running difference_update: ", s1)
#Loop Through Set Items with add() Method

s1={1,2,3,4,5}
s2={4,5,6,7,8}
for x in s2:
   s1.add(x)
print (s1)
#Join Python Sets Using "|" pipe Operator
#the union operator
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1|s2
print (s3)
#Join Python Sets update() Method
# update() method also joins the two sets, duplicates not allowed.
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.update(s2)
print (s1)