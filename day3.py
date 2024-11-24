################ Taking inputs in PYTHON

# num1 = input("Enter a number :")
# print(num1)
# num2 = float(input("Enter float number :"))
# print(num2)

# num1 = int(input("Enter number one : "))
# num2 =int( input("Enter number two : "))
# print("The sum of num1 and num2 is : ",num1 + num2)


################ CONDITION IN PYTHON

# # if the datatype is not specified then then it will be in string 
# value = input("Enter a number : ")

# if value.isdigit():
#     num = int(value)
#     print(f"Converted to integer {num}")
# elif '.' in value:
#     num = float(value)
#     print(f"convereted into float {num}")
# else:
#     print("Invalid number input")


# number = float(input("Enter the number :"))

# if number > 0:
#     print("The number is positive")
# elif number < 0:
#     print("The number is negative")
# elif number == 0:
#     print("The number is zero")
# else:
#     print("INVALID")



# x = 10
# if x > 5:
#     print("x is greater than 5")
# if x < 15:
#     print("X is less than 15")
# if x == 0:
#     print(f"{x} is zero")

# if x >= 5:
#     print("x is greater than 5")

# if x <= 15:
#     print("x is less than 15")


################ AND CONDITION
# x = 9

# if x > 5 and x < 10:
#     print(f"{x} is greater than 5 and less than 10")
# elif x == 5:
#     print(f"{x} is equal to 5")
# elif x == 10:
#     print(f"{x} is equal to 10")
# else:
#     print(f"{x} is not greater than 5 and less than 10")


################ OR CONDITION 

# x = 3

# if x > 2 or x < 10:
#     print(f"{x} is greater than 2 or less than 10")
# elif x == 2:
#     print(f"{x} is equal to 2")
# elif x == 10:
#     print(f"{x} is equal to 10")
# else:
#     print(f"{x} is NOT greater than 2 or less than 10")


################ TAKING STRING INPUT

# num = input("Enter the fruit : ")

# if num == "apple" or num == "orange":
#     print("The num is either the apple or the orange")
# else:
#     print(f"The fruit the user has entered is {num}")



################ USING NOT EQUAL TO

# num = int(input("Enter the number : "))
# if num != 5:
#     print("The number is not equal to 5.")


################ NESTED IN PYTHON -> try not to use nested more suggestion of the instructor.

# x = 5
# if x > 0:
#  if x < 10:
#   print("X is a positive single digit number.")
#  else:
#   print("X is a positive integer but not a single digit")
# else:
#     print("x is not a positive integer")
 


################  ONE LINE IF ELSE STATEMENT

# a = 20
# b = 30
# print(a + 1) if a > b else print(b + 1)

# a , b = 2 ,330
# sum = 1 if a  > b else 2
# print(sum)


# a = 100
# b  = 330

# if a > b:
#     print("A")
# else:
#     if a == b:
#         print("=")
#     else:
#         print("B")


################ SHORTHAND 
# print("A") if a > b else print("=") if a == b else print("B")

################ USING IF NOT IN PYTHON

# a = 100
# b  = 330

# if not a > b :
#     print("A is not greater than B")


################ if we want to put if statement with nothing inside of it we would rather put pass can't be left emptied

# a , b = 33,10

# if b > a:
#     pass

