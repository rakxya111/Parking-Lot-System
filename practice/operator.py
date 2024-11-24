x = 15 
y = 10

print("hello",1,2 , sep = "\t")
print("hello",1,2 , end = "\n")

############### logical operator

if x > 0 and y > 0 :
    print("both numbers x and y are greater than zero")

if x > 0 or y > 0:
    print("One of the number is greater than zero.")

if not(x < 0):
    print("X is not a negative number.")


############### membership operator :Membership operators in Python are used to test if a sequence (such as strings, lists, tuples, etc.) contains a certain element.
 
list = [1,2,3,4]

if 3 in list:
    print("Yes 3 is in the list.")

if 3 not in list:
    print("3 is not in the list")

############### identity operator : Identity operators in Python are used to compare the memory locations of two objects. They check whether two variables point to the same object in memory.

x = [1, 2, 3]
y = [1, 2, 3]
z = x

if x is z:
    print("both the x and z points the same object")

if x is not y:
    print("Both the x and y donot point out to the same object")

