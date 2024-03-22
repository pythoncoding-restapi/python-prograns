#forloop
for count in range(6):
   print ("Iteration no. {}".format(count))
else:
   print ("for loop over. Now in else block")
print ("End of for loop")
#For-Else Construct with forceful termination (with break statement)
for i in ['T','P']:
   print(i)
   break
else:
   # Loop else statement
   # terminated after 1st iteration due to break statement in for loop
   print("Loop-else statement successfully executed")
 # For-Else Construct with break statement and if conditions
# creating a function to check whether the list item is a positive
# or a negative number
def positive_or_negative():
   # traversing in a list
   for i in [5,6,7]:
   # checking whether the list element is greater than 0
      if i>=0:
         # printing positive number if it is greater than or equal to 0
         print ("Positive number")
      else:
         # Else printing Negative number and breaking the loop
         print ("Negative number")
         break
   # Else statement of the for loop
   else:
      # Statement inside the else block
      print ("Loop-else Executed")
# Calling the above-created function
      