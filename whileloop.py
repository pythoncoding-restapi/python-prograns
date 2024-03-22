#example of whilestat with else
k=0
# traversing until the condition is true(k<8)
while k<8:
   # incrementing the k value by 1
   k+=1
   # printing k value
   print("k =",k)
else:
   # else block gets executed when the condition fails(becomes false)
   print("This is an else block")
   #Using Else statement in While loop with a break statement

# creating a function that checks if the
# list passed to it contains an even number
def hasEvenNumber(l):

   # getting the list length
   n = len(l)
   # intializing a variable with 0(index)
   i = 0
   # traversing the loop until the I value is less than the list length
   while i < n:
   # checking whether the corresponding index element of a list is even

      if l[i] % 2 == 0:

         # printing some text, if the condition is true
         print("The input list contains an even number")

         # giving a break statement/break the loop

         break

         # incrementing the I (index) value by 1

      i += 1

   else:
   # Else print "The input list doesn't contain an even number"
   # It executes Only if the break is NEVER met and the loop is terminated after all iterations

      print("The input list doesn't contain an even number")

# calling the hasEvenNumber() function by passing input list 1 as an argument
print("For Input list 1:")
hasEvenNumber([3, 9, 4, 5])
# calling the hasEvenNumber() function by passing input list 2 as an argument
print("For Input list 2:")
hasEvenNumber([7, 3, 5, 1])