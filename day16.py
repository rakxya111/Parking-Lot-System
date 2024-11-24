
################## Map () function in PHP :

values = [1,2,3,4,5,6,7]

# altered = list(map(lambda x : x ** 2 , values))
# print(altered)



################## another method of using map() function for above program :

# values = [1,2,3,4,5,6,7]

# def squared(x): # map takes single parameter only 
#     return x ** 2

# square_number = list(map(squared,values))
# print(square_number)


################## NOTE :  map() -> if we want to alter each and every item then we use map.

# values = [1,2,3,4,5,6,7,8,9,10,11,12]
# even_numbers = list(map(lambda a : a % 2 == 0,values))
# print(even_numbers)


################## Filter() -> To store the values by filtering out we use filter (works on True or False)
##################  filter () using lambda :


# values = [1,2,3,4,5,6,7,8,9,10,11,12]
# even_numbers = list(filter(lambda a : a % 2 == 0,values))
# print(even_numbers)



############## Filter() -> using seprate function


# values = [1,2,3,4,5,6,7,8,9,10,11,12]

# def even_check(a):
#     return a % 2 == 0

# evenornot = list(filter(even_check,values))
# print(evenornot)


################## reduce() -> If the items of list or list of values are reduced to a single number then it is call reduce , NOTE : TO USE REDUCE first we need to import the reduce.


# from functools import reduce

# values = [1,2,3,4,5,6,7,8,9,10]
# sum = reduce(lambda x , y : x + y,values)
# print(sum)


################### finding the maximum number in the list 

# values = [3,8,1,6,2]
# max_num = reduce(lambda x , y : x if x > y else y,values)
# print(max_num)

################### concatenating string in the list

# words = ["Hello"," ","World","!"]
# sentence = reduce(lambda x , y : x + y , words)
# print(sentence)


###################  Using an initializer (MULTIPLICATION)

# numbers = [1,2,3,4,5]
# product = reduce(lambda x , y : x * y , numbers,1)
# print(product)




################## ASSIGNMENT : (USE MAP , FILTER OR REDUCE)
 

################## Q1 : convert the string to the uppercase : words = ["abc", "csv","json"] 


# words = ["abc", "csv","json"] 

# def uppercase(a):
#     return a.upper()

# upper_words = list(map(uppercase,words))
# print(upper_words)



################## Q2 : Get words with more than 4 letters : words = ["cat","elephant","dog","giraffe","bird"]


# words = ["cat","elephant","dog","giraffe","bird"]

# def Isfourletter(a):
#     if len(a) == 4:
#         return True 

# fourletter = list(filter(Isfourletter,words))
# print(fourletter)


################## Q3 : Remove all the odd numbers and square the even numbers

# numbers = [1,2,3,4,5,6,7,8,9,10]

# def alteration(a):
#     if a % 2 == 0:
#         return True
         

# even = list(filter(alteration,numbers))
# square = list(map(lambda a : a * a,even))
# print(square)


################## Q4 : convert temperature from celsius to fahrenheit


# tempC = [12,13,14,70]

# def fahrenheit(a):
#     a = a * 9/5 + 32
#     return a

# tempF = list(map(fahrenheit,tempC))
# print(tempF)



################## Q5 :  Remove all the even numbers less than 10 from the list  
# 1 : square the remainaing numbers 
# 2: sum the squared number


from functools import reduce

list1 = [1,2,4,6,3,11,12,13,14,15]

def lessten(a):
    if a % 2 == 0 and a < 10:
        return False
    else:
        return True

lessT = list(filter(lessten,list1))
square = list(map(lambda a : a * a,lessT))
sum = reduce(lambda x , y : x + y,square)
print(sum)

#################### ANOTHER WAY OF ABOVE QUESTION : 


from functools import reduce

list1 = [1,2,4,6,3,11,12,13,14,15]

lessTen = list(filter(lambda x  : False if x % 2 == 0 and x < 10 else True,list1))
square = list(map(lambda a : a * a,lessTen))
sum1 = reduce(lambda x , y : x + y , square)
print(sum1)