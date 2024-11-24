############################# MODULE FILE MADE TO IMPORT AS MODULE ###################################


def sum(a , b):
    return a + b

def difference(a , b):
    return a - b 

def multiplication(a , b):
    return a * b 

def divison(a , b):
    return a / b 

# print("This is a calculator")    # NOTE: will print wherever it has been imported cause it's written outside and the whole file gets compiled from top to bottom line by line So if we want to avoid this then we can also use the below code.


########### if we add the below code then it won't be printed once it has been imported automatically.

if __name__ == "__main__":  # will not print wherever it has been imported automatically
    print("This is a calculator") 




person = {
    "name" : "Rakshya",
    "age" : 21
        
    }