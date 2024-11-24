
# class person:

#     def name(self,name,age):
#         self.name = name
#         self.age = age
#         print(f"The name is {self.name} and age is {self.age}.")

# obj = person()
# obj.name("Tina",18)




# class person:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def print(self):
#         return self.name

# class family(person):

#     def __init__(self, name, age):
#         super().__init__(name, age)
#         print(print())

# new = family("shila",18)





# class Area:

#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
    
#     def area(self):
#         return self.length * self.breadth
    

# class rectangle(Area):
#     def __init__(self, length,breadth):
#         super().__init__(length,breadth)

# class square(Area):
#     def __init__(self, length):
#         super().__init__(length , length)

# area = Area(10,20)
# rectangle = rectangle(13,10)
# square = square(12)
# print(rectangle.area())
# print(square.area())
      

class person :

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sound(self):
        print(f"Name : {self.name} , Age : {self.age} ")
    
class detail(person):

    def __init__(self,name,age,hobby):
        super().__init__(name,age)
        self.hobby = hobby
    
    def print(self):
        s = super().sound()
        print(f"The hobby of {self.name} of age {self.age} is {self.hobby}.")


obj = detail("Hania",13,"painting")
obj.print()
