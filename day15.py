################  MODULE IN PYTHON
############### Here we might have created a mymodule or any name python file then that file can be imported here in our current file as module by using import keyword


# import mymodule

# print(mymodule.sum(2,3))
# print(mymodule.difference(10,3))
# print(mymodule.multiplication(90,3))
# print(mymodule.divison(18,3))


############### If the module file is in another folder then we also need to mention the folder name follwing with the module filename 

################# NOTE : when the name of the file is long then we can use (as) following with the name we want to give such as above it's mod

# import package.module1 as mod                                                              
 
# print(mod.sum(2,3))
# print(mod.difference(10,3))
# print(mod.multiplication(90,3))
# print(mod.divison(18,3))


################ NOTE : In python we can also import selective things from the module file by using the (from module-name import selected-module-portion as custom-name) format 


# import mymodule as mod
# from mymodule import sum as add, difference as sub    # importing selectively

# print(add(2,3)) # NOTE : if we do import and rename then no need to mention module name
# print(sub(10,3))




#################  When we want to import selective portion we dodnot need to write (import module-name) on top just start with from...


# from mymodule import person   # importing only person dict from mymodule 

# print(person["name"])
# print(person["age"])



################## DECORATOR -> The decorator are used on such cases when we need to add something into the program but it's way too long soo then we just use decorator and then add the decorator above the program . Also used to calculate the amount of time 


# def decorator1(fun):
#     def wrapper():
#         print("Something Before Function runs")
#         fun() # becomes say_hello()NOTE:here instead of fun() can add any variable instead like a()
#         print("Something AFter Function runs")
#     return wrapper


# @decorator1
# def say_hello():
#     print("hello")
# say_hello()


################### Decorator : (Taking arguments)


# def decorator1(fun):
#     def wrapper(*args,**kwargs):
#         print("Something Before function runs")
#         fun(*args,**kwargs)
#         print("Something AFter Function runs")
#     return wrapper

# @decorator1
# def say_hello(a,b):
#     print("The sum is :", a + b)

# say_hello(2,3)


################# NOTE : There are usually in-built decorator but if we want to create custom decorator then we can follow the above instructions.


def great_decorator(greetings):

    def decorator1(fun):
        def wrapper(*args,**kwargs):
            print(f"{greetings} Something before Function runs")
            fun(*args,**kwargs)
            print("Something After Function runs")
        return wrapper
    return decorator1


@great_decorator("hello world")

def say_hello(a,b):
    print("a and b is : ",a,b)

say_hello(20,34)