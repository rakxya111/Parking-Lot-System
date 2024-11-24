################# EXCEPTION HANDLING IN PYTHON-> try,except, finally 

################# NOTE->(we would try out a program and then if it works out then good but then if it doesnot works out then the program would get crashed so in order to prevent that we would use exception handling to handle the error if encountered without letting the program to be crashed.)


# def divide(x,y):
#     try:
#         result = x/y
#     except ZeroDivisionError:
#         print("Error divison by zero !")
#     except TypeError as e:
#         print(f"ERROR : {e}")
#     else:
#         print(f"Result : {result}")
#     finally:
#         print("Execution completed !")
    

# divide(10,0)
# divide(10,"a")
# divide(10,2)



################# CUSTOM EXCEPTION :

# try:
#     a = int(input("Enter a number : "))
#     # a = -1

#     # if a < 0:
#     #     raise Exception("The number should not be less than zero.")
# except Exception as b:
#     print(f"B:{b}")
# finally:
#     print("\nEnd of the program.")



################### EXCEPTION IN CLASS :



# class mycustomerror(Exception):
    
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)
    



################### RAISE :



# try :
#    x = int(input("enter num :"))
#    if x < 0:
#         raise Exception("Custom error")

# except Exception as e:
#     print(e)
#     print("This is an exception.")




################### TRACEBACK :



# import traceback
# def divide(x,y):
#     try:
#         result = x + y
#         result1 = x - y
#         result2 = x / y
    
#     except Exception as e:
#         print(f"General Exception {e}")
#         traceback.print_exec()  # printouts the line where the error has been encountered.

# divide(1,0)




################### CLASS ASSIGNMENT :



# dict1 = {
#     "name" : "abc",
#     "address"  : "ktm"
# }


# try:
#     print(dict1["email"])

# except Exception as e:
#     dict1["email"] = input("enter as email :")
#     print("email entered")
#     print(dict1["email"])
    
try:
    a = input("enter anything :")

    if (a == "exit"):
        exit
    elif(int(a) < 5 or int(a) > 9):
        raise ValueError("Error encountered.")

finally:
    print("eof")
