############### PYTHON CLASS -> keyword -> class className 
#contrsuctor syntax : __init__


# class Person:

#     def getname(self,name):
#         self.name = name
#         print("Name is :",self.name)

#     def __init__(self,name,age): 
#         self.name = name
#         self.age = age 
#         print("Hello my name and age is ",self.name,self.age)



# p1 = Person("rakshya",21)
# p1.getname("dhiraj")
# print(p1.name)
# print(p1.age)

# lst = "hello"
# lst.strip()


############### INHERITANCE IN PYTHON :

############### SINGLE INHERITANCE :


# class animal:

#     def speak(self,name):
#         self.name = name
#         print("The name of animal is : ",self.name)
#         return self.name
    
# class dog(animal):

#     def bark(self,sound):
#         self.sound = sound
#         print("The sound of animal is : ",self.sound)
#         return self.sound

# my_dog = dog()
# my_dog.bark("hwau hwau")
# print(my_dog.bark())
# my_dog.speak("dog")
# print(my_dog.speak())



############### MULTIPLE INHERITANCE :

# class A:
#     def method_A(self):
#         return "Method A"

# class B:
#     def method_B(self):
#         return "Method B"

# class C(A,B):
#     def method_A(self): #same method name as parent class 
#         return "Method C"
    
# obj_c = C()
# print(obj_c.method_A()) # now it will call method of c not a 
# print(obj_c.method_B())



############### MULTI-LEVEL INHERITANCE :

# class A:
#     def method_A(self):
#         return "Method A"

# class B(A):
#     def method_B(self):
#         return "Method B"
    
#     def method_A(self):
#         return "From method B" 

# class C(B):
#     def method_C(self): 
#         return "Method C"

# obj_C = C()
# print(obj_C.method_A())
# print(obj_C.method_B())
# print(obj_C.method_C())



############### Super() keyword : In Python, super() is a built-in function that is used to call methods of a superclass (parent class) in a subclass (child class).


# class Rectangle:

#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
    
#     def area(self):
#         return self.length * self.breadth
    
# class Square(Rectangle):

#     def __init__(self,side_length):
#         super().__init__(side_length, side_length)

# Rectangle = Rectangle(10,20)
# Square = Square(20)

# print("The area of Rectangle is :",Rectangle.area())
# print("The area of Square is :",Square.area())



################## CLASS ASSIGNMENT :


class Animal:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):

    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
       s = super().speak()
       print(f"{self.name} say bark")


new_dog = Dog("dog",24,"xyz")
print(new_dog.age)
new_dog.speak()

