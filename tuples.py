# index inside square brackets to retrieve the item at its position.

tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)

print ("Item at 0th index in tup1tup2: ", tup1[0])
print ("Item at index 2 in list2: ", tup2[2])
#Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#update we convert the tuple to a list, update an existing item, append a new item and sort the list. The list is converted back to tuple.

tup1 = ("a", "b", "c", "d")
print ("Tuple before update", tup1, "id(): ", id(tup1))

list1 = list(tup1)
list1[2]='F'
list1.append('Z')
list1.sort()
print ("updated list", list1)

tup1 = tuple(list1)
print ("Tuple after update", tup1, "id(): ", id(tup1))
 #tuple is unpacked in individual variables
tup1 = (10,20,30)
x, y, z = tup1
print ("x: ", x, "y: ", "z: ",z)

#tuples in loop
tup1 = (25, 12, 10, -21, 10, 100)
indices = range(len(tup1))
for i in indices:
   print ("tup1[{}]: ".format(i), tup1[i])
 # concatenation for tuples

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = T1+T2
print ("Joined Tuple:", T3)
#extend method
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
L1 = list(T1)
L2 = list(T2)
L1.extend(L2)
T1 = tuple(L1)
print ("Joined Tuple:", T1)
# augmented concatenation operator with the "+=" symbol to append T2 to T1

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T1+=T2
print ("Joined Tuple:", T1)
#for loop in tuple
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
for t in T2:
   T1+=(t,)
print (T1)
(10, 20, 30, 40, 'one', 'two', 'three', 'four')
#tuple indexmethod
tup1 = (25, 12, 10, -21, 10, 100)
print ("Tup1:", tup1)
x = tup1.index(10)
print ("First index of 10:", x)

#tuple count methods
tup1 = (10, 20, 45, 10, 30, 10, 55)
print ("Tup1:", tup1)
c = tup1.count(10)
print ("count of 10:", c)
