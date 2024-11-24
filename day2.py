################ basics of python (STARTING)
# name = "hello"
# Name = "world"
# my_name = "rakshya"
# print("name",name)
# print("name",Name)
# print("name is",my_name)
# total_count = 5 #snake cases
# print("count is :",total_count)
# print(name,total_count,my_name)

# x = 15 
# y = 10

# print("hello",1,2 , sep = "\t")
# print("hello",1,2 , end = "\n")

################ updating variables in python - it is a interpretor language

# print("updating values:")
# x = 5
# print(x)
# x = 6 #after updating
# print(x)

################ storing multiple values 
################ Assining multiple values in python


# x , y , z = 1 ,2 ,3
# r , z, t = "reema",2 , "dina"
# print("printing multiple values : ",r,z,t)


################ Arthimetic operation in python

# m , k = 100 ,20
# print("arithmetic operation in python \n")
# print ("addition  of m and k is : ", m + k)
# print ("subtraction  of m and k is : ", m - k)
# print ("Multipliaction  of m and k is : ", m * k)
# print ("Divison  of m and k is : ", m/k)
# print ("floor Divison  of m and k is : ", m//k)
# print ("modulo  of m and k is : ", m % k)
# print ("Exponentiation  of m and k is : ", m ** k)

# f_name , L_name = "Alia" , "Bhatt"
# print (f_name + L_name)


################ Types of operators in python -: arithimtic , comparison, logical , membership , identity , assignment
################## membership operator = in , not in 
################## identity operator = is , is not

# print (" Using Assignment operators in Python \n")
# al = 10

# al += 1
# print("Addition assignment operator :", al)
# al -= 1
# print("Subtaction assignment operator :",al)
# al *= 1
# print(" Multiplication assignment operator :", al)
# al /= 1
# print(" Divison assignment operator :", al)
# al %= 1
# print(" Modulo assignment operator :", al)
# al //= 1
# print(" floor divison operator :", al)
# al **= 1
# print(" Exponentiation operator :", al)

################ Logical operator (and , or , not)

# if x > 0 and y > 0 :
#     print("both numbers x and y are greater than zero")

# if x > 0 or y > 0:
#     print("One of the number is greater than zero.")

# if not(x < 0):
#     print("X is not a negative number.")


# ############### Membership operator :Membership operators in Python are used to test if a sequence (such as strings, lists, tuples, etc.) contains a certain element.
 
# list = [1,2,3,4]

# if 3 in list:
#     print("Yes 3 is in the list.")

# if 3 not in list:
#     print("3 is not in the list")

# ############### Identity operator : Identity operators in Python are used to compare the memory locations of two objects. They check whether two variables point to the same object in memory.

# x = [1, 2, 3]
# y = [1, 2, 3]
# z = x

# if x is z:
#     print("both the x and z points the same object")

# if x is not y:
#     print("Both the x and y donot point out to the same object")

################# COMPARISON OPERATOR IN PYTHON
# print("\nCOMPARISON OPERATOR IN PYTHON\n")
# ab , bc = 1 , 0
# print("ab and bc is equal or not : ", ab == bc)
# print("ab and bc is not equal or not : ", ab != bc)
# print("ab and bc is greater  or not : ", ab > bc)


################## LOGICAL OPERATOR IN PYTHON

# # x , y = 5,10
# # if x > 5 and x < 10:
# #     print("true")

# x = ["apple", "banana"]
# print("banana" in x)
# print("banana" not in x)

# print ("The data type of x is :", type(x))
# i = 4
# print ("The data type of x is :", type(i))
# j = "5"
# print ("The data type of x is :", type(j))

################## DATATYPES IN PYTHON

################## string

# r = "Hello world" 
# print("\n")
# print(r)
# print ("The data type of r is :", type(r))

################## range

# r = range(10) 
# print("\n")
# print(r)
# print ("The data type of r is :", type(r))

################## complex

# r = 1j 
# print("\n")
# print(r)
# print ("The data type of r is :", type(r))

################## list

# r = ["apple","banana"] 
# print("\n")
# print(r)
# print ("The data type of r is :", type(r))

################# tuple

# r = ("apple","ball") 
# print("\n")
# print(r)
# print ("The data type of r is :", type(r))

################## dict

# r = {"name" : "John", 
#      "age" : 36 }
# print("\n")
# print(r)
# print ("The data type of r is :", type(r))

################## set

# r = {"apple", "ball"}
# print("\n")
# print(r)
# print ("The data type of r is :", type(r))

################## frozen set

# r = ({"apple","cat","dog"})
# print("\n")
# print(r)
# print ("The data type of r is :", type(r))

################## boolean

# r = True
# print("\n")
# print(r)
# print ("The data type of r is :", type(r))


################## converting the values to integer in python

# h = int(1)
# l = int(1.2)
# b = int("3")
# # v = int("s") #doesnot convert
# # f = int("sam") #doesnot convert
# print(h,l,b)


################## converting the values to float in python

# h = float(1)
# l = float(1.2)
# b = float("3")
# y = float("3.8")
# print(h,l,b,y)

################## converting the values to string in python

# h = str(1)
# l = str("sarita")
# b = str("3")
# y = str("3.8")
# print(h,l,b,y)

################## converting list to tuple
################## list can be converted into tuple and vice versa and list is also faster and list can also be converted into set , set cannot be converted and list can also cannot be manipulated

# r = tuple(["apple","banana"]) #converting list into tuple





