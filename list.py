#access item from list by index no
list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]

print ("Items from index 1 to 2 in list1: ", list1[1:3])
print ("Items from index 0 to 1 in list2: ", list2[0:2])
 #list is changeable
list3 = [1, 2, 3, 4, 5]
print ("Original list ", list3)
list3[2] = 10
print ("List after changing value at index 2: ", list3)

#append method insert items at the end

list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list1.append('e')
print ("List after appending: ", list1)
 #insert method inserts the item at a specified index in the list.

list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list ", list1)

list1.insert(2, 'Chemistry')
print ("List after appending: ", list1)

list1.insert(-1, 'Pass')
print ("List after appending: ", list1)
 #remove() method removes the specified item from the list.

list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)

list1.remove("Physics")
print ("List after removing: ", list1)
# pop() method removes the specified item from the list based on the given index.

list2 = [25.50, True, -55, 1+2j]
print ("Original list: ", list2)
list2.pop(2)
print ("List after popping: ", list2)
#Remove Specified List Item Using del Keyword
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
del list1[2]
print ("List after deleting: ", list1)

#Remove Consecutive List Items

list2 = [25.50, True, -55, 1+2j]
print ("List before deleting: ", list2)
del list2[0:2]
print ("List after deleting: ", list2)
 # Loop Through List Items with Index
lst = [25, 12, 10, -21, 10, 100]
indices = range(len(lst))
for i in indices:
   print ("lst[{}]: ".format(i), lst[i])
#Sort List Items Alphanumerically
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print ("list before sort", list1)
list1.sort()
print ("list after sort : ", list1)

print ("Descending sort")

list2 = [10,16, 9, 24, 5]
print ("list before sort", list2)
list2.sort()
print ("list after sort : ", list2)
#Example of Copy List in Python
lst = [10, 20]
lst1 = lst.copy()
print ("lst:", lst, "id(lst):",id(lst))
print ("lst1:", lst1, "id(lst1):",id(lst1))
#Join Python Lists Using Augmented Concatenation Operator
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L1+=L2
print ("Joined list:", L1)
# using the extend() method

L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L1.extend(L2)
print ("Joined list:", L1)
# Join Python Lists by Appending Items

L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']

for x in L2:
   L1.append(x)
   
print ("Joined list:", L1)
