############ .isdigit() METHOD IN PYTHON

# s = "stringg"
# print(s.isdigit()) #output : false

# s = "234455"
# print(s.isdigit()) #output : true


############ .isupper() , .islower() METHOD IN PYTHON

# s = "stringg"
# print(s.isupper()) # output : false

# s = "stringg"
# print(s.islower()) # output : true


############## .format() -> method -> This method formats the string , replacing placeholders with the values 

# s = "hello, {}!" #curly bracket vtra aba world vanne basxa 
# print(s.format("world"))

# s = "hello, {} {}!" #curly bracket vtra aba world  ani whatsup vanne basxa (multiple ni rakhna milxa) 
# print(s.format("world","whatsup"))

################ F-string

# a = 5
# b = 6
# s = f"The sum of {a} and {b} is {a + b}."
# print(s)


############### ESCAPE CHARACTER

# text = "We are so-called \"Vikings\" from the north "
# print(text)


############### LIST OF MIXED DATATYPES INSIDE THE LIST

# mixed_list = ['1' , "hello" , 2 ,True]
# print(mixed_list)


################ ACCESSING INDEX IN MIXED LIST


# mixed_list = ['1' , "hello" , 2 ,True]
# print(mixed_list[-1])
# print(mixed_list[2:3])
# print(mixed_list[2:])
# print(mixed_list[:3])



################ CHANGING ELEMENT IN LIST

# values = [1,2,3,4,5,6]
# fruits = ['apple','banana','strawberry']
# fruits[1] = "orange" # we can change elements in case of list
# print(fruits)


################# [APPEND] Adding elements in LIST

# fruits = ['apple','banana','strawberry']
# fruits.append('blueberry')
# print(fruits)


################## [REMOVE] Removing elements in LIST

# fruits = ['apple','banana','strawberry']
# fruits.remove('banana')
# print(fruits)


################### UPDATING ELEMENT IN THE PARTICULAR INDEX IN LIST

# fruits = ['apple','banana','cherry','strawberry']
# print(fruits)
# for i in range(len(fruits)):
#     if fruits[i] == 'cherry':
#         fruits[i] = 'mango'

# print(fruits)    


# fruits = ['apple','banana','cherry','strawberry']
# print("These are the fruits :",fruits)
# name = input("enter the value to be replaced with  : ")

# for i in range(len(fruits)):
#     if fruits[i] == 'cherry':
#         fruits[i] = name

# print(fruits)  


# fruits = ['apple','banana','cherry','strawberry']

# for i in fruits:
#     print(i)

# fruits = ['apple','banana','cherry','strawberry']
# index = 0
# while index < len(fruits):
#     print(fruits[index])
#     index += 1



############ ASSIGNMENT

###############  write a program to append the item in list but the value to be append should not be in the list.

##############  [METHOD 1]:

# fruits = ['apple', 'banana', 'cherry', 'strawberry']
# new_fruit = input("Enter the fruit to be appended: ")


# if new_fruit in fruits:
#     print(f"{new_fruit} already exists in the list.")
#     print(fruits)
# else:
#     fruits.append(new_fruit)
#     print(f"{new_fruit} has been added to the list.")
#     print("Updated list of fruits:", fruits)


###############  [METHOD 2] :   
 
# fruits = ['apple', 'banana', 'cherry', 'strawberry']
# new_fruit = input("Enter the fruit to be appended: ")

# flag = 0
# for i in range(len(fruits)):
#     if fruits[i] == new_fruit:
#         print(f"{new_fruit} already exits in the list")
#         flag = 1
#         break

# if(flag == 0):
#     fruits.append(new_fruit)

# print(fruits)
