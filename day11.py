################ PYTHON IS Operator :

# x = None
# y = None

# print(x is None)  # output : true
# print(y is None)  # output : true

# z = 5
# print(z is None)  # output : false


""" 

PYTHON FUNCTION -> def keyword
SYNTAX : def function_name(parameters):
         return expression
function call : function_name(arguements)

"""

################ SUM using functions : (BASIC CONCEPT)

# def sum_numbers(a,b):
#     sum = a + b
#     return sum

# a  , b = 10, 12
# sum_value = sum_numbers(a,b)
# print(f"The sum of {a} and {b} is : ", sum_value)


################ ANOTHER WAY of performing SUM using functions :

# def sum_numbers(a,b):
#     sum = a + b
#     print(f"The sum of {a} and {b} is : ",sum)

# sum_numbers(10,20)
# or sum = sum_numbers(10,20) and then next line print(sum) -> output will be None cause nothing has been returned


################# USING TUPLE IN FUNCTION IN PYTHON :

# def get_stats(numbers):
#     min_value = min(numbers)
#     max_value = max(numbers)
#     sum_value = sum(numbers)
#     return min_value, max_value,sum_value # Returning multiple values from function

# numbers = [1,2,3,4,5,6,7,8]
# min , max , sum = get_stats(numbers) # Unpacking variables and calling the fucntion

# print("The minimum value is : ",min)
# print("The maximum value is : ",max)
# print("The sum of all values is : ",sum)


################ USING LIST IN FUNCTION IN PYTHON

# def get_stats(numbers):
#     min_value = min(numbers)
#     max_value = max(numbers)
#     sum_value = sum(numbers)
#     return [min_value, max_value,sum_value] #returning multiple values from function

# numbers = [1,2,3,4,5,6,7,8]
# stats = get_stats(numbers)  # calling the function AND SENDING ARGUEMENTS IN A LIST

# print("The minimum value is : ",stats[0])
# print("The maximum value is : ",stats[1])
# print("The sum of all values is : ",stats[2])


################ USING DICTIONARY IN FUNCTION IN PYTHON

# def get_stats(numbers):
#    return  {
#       "min" : min(numbers),
#       "max" : max(numbers),
#       "sum" : sum(numbers)
#    }


# numbers = [1,2,3,4,5,6,7,8]
# stats = get_stats(numbers) #  calling the fucntion

# print("The minimum value is : ",stats["min"])
# print("The maximum value is : ",stats["max"])
# print("The sum of all values is : ",stats["sum"])


################ Default Arguement IN PYTHON

# def addition(a,b=2):
#     return a + b

# print(addition(10))


################ Local Variable -> CAN'T BE ACCESSED OUTSIDE FUNCTION OR ANYWHERE

# def my_function():
#     x = 10
#     print("inside function :",x)

# my_function()
# # print(x) #error


################# Global Variable -> CAN ALSO BE ACCESSED OUTSIDE THE FUNCTION OR ANYWHERE

# x = 10
# def my_function():
#     print("inside function :",x)

# my_function()
# print("Outside function",x) 


################# USING GLOBAL KEYWORD -> to make the variable global inside the function 

# def my_function():
#     global x 
#     x = 10
#     print("inside function :",x)

# my_function()
# print("Outside function",x) 



################ IMPORTANT AND NEW CONCEPT :
################ ARBITARY ARGUEMENT (*args) -> send arguements as tuple as much as we want and then using * in parameter so that we donot have to mention multiple parameters.


# def my_function(*kids):
#     print("The youngest kid is", kids[2])

# my_function("hari","shyam","ram","badri","komal","chaya")


################ ARBITARY K WORD ARGUEMENT (**kwargs) -> send multiple arguements with default value and then in parameter section using ** to access the arguements.


# def my_function(**kids):
#     print("The last name  is", kids["lname"])

# my_function(lname = "kwagrs",fname = "ram") # NO DOUBLE CODE IN ARG ONLY USED IN VALUE OF ARG 


# def my_function(**kids):
#     print(kids)

# my_function(lname = "kwagrs",fname = "ram")


################ USING BOTH *args and **kwargs 

# def my_function(*args,**kwargs):
#     for arg in args:
#         print(arg)
    
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# my_function("ram","shyam",fname = "rakshya",lname = "bhuju") # NOW ONCE THE DEFAULT ARGUMENT WITH VALUE IS WRITTEN WE CANNOT NOW WRITE ONLY ARGUMENT


################ LAMMBDA IN PYTHON -> USED FOR SINGLE LINE CODE 
# SYNTAX -> lamda arguements : expression

# x = lambda z : z + 10
# print(x(100))

# x = lambda z ,x : x * z
# print(x(100,120))


################ RECURSION IN PYTHON :

################ FACTORIAL USING RECURSION IN PYTHON :

# def fact(a):
#     if a == 0 or a == 1:
#         return 1
    
#     else:
#         return a * fact(a-1)
    
# print(fact(7))



################ RECURSION IN PYTHON ASSIGNMENT : LAMDA FUNCTION SQUARE NUMBER , CHECK IF NUMBER IS EVEN

################# LAMDA FUNCTION SQUARE NUMBER :

num = lambda a : a * a
print("The square of a number is :",num(2))

################ CHECK IF NUMBER IS EVEN OR NOT :

even_number = lambda b : b % 2 == 0 
input = int(input("enter a number to check even or not : "))
value = even_number(input)

if value == True:
    print("EVEN")
else:
    print("ODD")

################ H.W. ASSIGNMENT : FIBONACCI USING RECURSION

def fibonacci(a):

    if a == 0 or a == 1:
        return 1
    
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)

number = int(input("Enter a number to find out fibonacci : "))

print(f"Fibonacci of {number} is :")
for num in range(number):
   print(fibonacci(num) , end = '\t' )

    