################ ABSTRACTION AND ACCESS SPECIFIERS :


# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod # jun method lai call garxa jun class le tesma tyo method exists garna prxa 
#     def makesound(self):
#         print("asdff")
#         pass

# class Dog(Animal):
#     pass

#     # def makesound(self):
#     #     return "woof !"
    

# dog = Dog()
# print(dog.makesound())



################  ACCESS MODIFIER :


################ PUBLIC ACCESS MODIFIER :- Attributes and methods without any leading underscore (_) are considered public and can be accessed from anywhere, both within the class and outside the class.


# class myclass:
#     def __init__(self):
#         self.public_name = "Public varible"
    
#     def public_method(self):
#         return "This is a public method and it can be accessed from anywhere."

# obj = myclass()
# print(obj.public_name)
# print(obj.public_method())



################ PRIVATE ACCESS MODIFIER :- Attributes and methods with a double underscore (__) prefix are conventionally considered private. 


# class myclass:

#     def __init__(self):
#         self.__private_name = "private variable"
#     def __private_method(self):
#         return "This is a private method and can't be accessed from outside."

# obj = myclass()
# # print(obj.__private_name) # error encountered
# print(obj.__private_method) # error encountered



################ PROTECTED ACCESS MODIFIER :- Attributes and methods with a leading underscore (_) are conventionally considered protected. They should not be accessed directly from outside the class, but can be accessed from within the class and its subclasses.

# class myclass:

#     def __init__(self):
#         self._protected_var = "Protected variable"
    
#     def _protected_method(self):
#         return "This is a protected method"

# obj = myclass()
# print(obj._protected_var) 
# print(obj._protected_method()) 



############### CLASS ASSIGNMENT : MAKING SIMPLE CALCULATOR


# class calculator:

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def addition(self):
#         print(f"{self.a} + {self.b} = ",self.a + self.b)
        
#     def subtraction(self):
#         print(f"{self.a} - {self.b} = ",self.a - self.b)
    
#     def multiplication(self):
#         print(f"{self.a} * {self.b} = ",self.a * self.b)
    
#     def divison(self):
#         print(f"{self.a} / {self.b} = ",self.a / self.b)
    

# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))
# calc = calculator(a,b)
# calc.addition()
# calc.subtraction()
# calc.multiplication()
# calc.divison()


################### CLASS ASSIGNMENT : 
 

# class vehicle:

#     def __init__(self,name,model,color):
#         self.name = name
#         self.model = model
#         self.color = color
    

# class car(vehicle):

#     def __init__(self, name, model, color):
#         super().__init__(name, model, color)
    
#     def opendoor(self):
#         print(f"The door is OPENed \n car name = {self.name} \n car model = {self.model} \n car color = {self.color}")
    
#     def closedoor(self):
#         print(f"The door is CLOSEed  \n car name = {self.name} \n car model = {self.model} \n car color = {self.color}")
    
    

# class motorbike(vehicle):

#     def __init__(self, name, model, color):
#         super().__init__(name, model, color)
    
#     def start(self):
#         print(f"The motorbike has been started . \n Motorbike name = {self.name} \n Mototrbike model = {self.model} \n Motorbike color = {self.color}")
    
#     def breakk(self):
#         print(f"The motorbike is hold on break. \n Motorbike name = {self.name} \n Motorbike model = {self.model} \n Motorbike color = {self.color}")
    
# obj = car("Toyota",1998,"red")
# obj1 = motorbike("Pulsar",1908,"blue")

# obj.opendoor()
# obj.closedoor()

# obj1.start()
# obj1.breakk()