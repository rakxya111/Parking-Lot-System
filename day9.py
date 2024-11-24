############### DAY 9 -> TUPLE

############### UNPACKING VARIABLES Using Asterisk : green variable would contain apple and yellow var will contain banana and others all others would be assigned to orange by using asterisk in orange.

# fruits = ("apple","bananna","cherry","strawberry","mango","litchi")
# (green,yellow,*orange) = fruits
# print(green)          # green = ("apple")
# print(yellow)         # yellow = ("banana")
# print(orange)         # orange = ("cherry",strawberry","mango","litchi")

# fruits = ("apple","bananna")
# (green,yellow,*orange) = fruits
# print(green)
# print(yellow)
# print(orange) #empty

# fruits = ("apple","bananna","cherry","strawberry","mango","litchi")
# (green,*yellow,orange) = fruits
# print(green)
# print(yellow) # yellow = ("bananna","cherry","strawberry","mango")
# print(orange)



################################################ SETS ################################################

################ PYTHON SETS -> doesnot have index and will not print repeted value


# myset = {"apple","orange","banana"}
# for i in myset:
#     print(i)
 
################ NOTE : True and 1  and then 0 and false is considered same. 

# empty_dit = {} # THIS IS EMPTY DICTIONARY
# empty_set = set()  # THIS IS EMPTY SET (empty set should be written by declaring the set and using small brackets)


################# ADDING in set -> only one element could be append with add method in set

# myset = {"apple","orange","banana"}
# myset.add("mango")
# print(myset)

################# Use UPDATE METHOD IN SET to append multiple values in set -> .update()

# myset1 = {"apple","orange","banana"}
# myset2 = {"mango","litchi","strawberry"}
# myset1.update(myset2)
# print(myset1)


################# REMOVE SET ITEMS : 

################# Remove method : -> if the element that is to be remove doesnot exist it would show error.

# myset1 = {"apple","orange","banana"}
# myset1.remove("banana")
# print(myset1)

# myset1 = {"apple","orange"}
# myset1.remove("banana") # does show error 
# print(myset1)

################# Discard method : -> if the element that is to be remove doesnot exist it would NOT show error.

# myset1 = {"apple","orange","banana"}
# myset1.discard("banana")
# print(myset1)

# myset1 = {"apple","orange"}
# myset1.remove("banana") # No error
# print(myset1)


################ POP Method -> Used to remove random item by pop

# myset = {"apple","orange","banana"}
# x = myset.pop() # popped value is stored in x
# print(myset)
# print(x)

################  Del keyword and Clear can also be used

################ WE SPECIFICALLLY USE SET To use Union , Update , Intersection , Difference and Symmetric_Difference.



################# UNION METHOD : (only works in list and tuple) -> in this just as in maths all the elements of both the sets are joined.

# set1 = {"a","b","c"}
# set2 = {1,2,3}

# set3 = set1.union(set2)
# print(set3)

################# another method of using union by using | opeartor

# set1 = {"a","b","c"}
# set2 = {1,2,3}

# set3 = set1 | set2 
# print(set3)

################ Multiple sets with union 

# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set3 = {4,5,6,7}
# set4 = {"elena" , "damon","stefan"}

# set5 = set1 | set2 | set3 | set4  # OR set5 = set1.union(set2,set3,set4)
# print(set5)


################ Intersection method : -> common elements in both the sets are assigned to new set.

# set1 = {"a","b","c"}
# set2 = {1,2,3,"a","b"}
# set4 = {"a","b",3,5}
# set6 = {"a",7,8,9}
# set8 = {"a","elena","damon"}
# set3 = set1.intersection(set2,set4,set6,set8)
# print(set3)


################  we can use & symbol to use interesection method as well

# set1 = {"a","b","c"}
# set2 = {1,2,3,"a","b"}
# set = set1 & set2
# print(set)

################ Instead of making new variable , Existing mai update grna pryo vane intersection_update() and union_update() yesari _update() use garxau.

# set1 = {"a","b","c"}
# set2 = {1,2,3,"a","b"}
# set1.intersection_update(set2)
# print(set1)

############### Differnce method -> agadi j xa tei hisab le print hunxa suppose tala set1 agadi xa

# set1 = {"a","b","c"}
# set2 = {1,2,3,"a","b"}
# set3 = set1.difference(set2)
# print(set3)

############### differnce_update method in order to assigned the elements to existing variable

# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set1.difference_update(set2)
# print(set1)

###############  WE can use - (minus) operator to represent difference method

# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set3 = set1 - set2
# print(set3)

################ SYMMETRIC DIFFERNCE METHOD : (dubai ma navako elements ko set banaunu)

# set1 = {"a","b","c","d"}
# set2 = {1,2,3,"a","b"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

################ Operator ^ is used for symmetric_difference method

# set1 = {"a","b","c","d"}
# set2 = {1,2,3,"a","b"}
# set3 = set1 ^ set2
# print(set3)

################ To Update in existing variable we use symmetric_difference_update()

# set1 = {"a","b","c","d"}
# set2 = {1,2,3,"a","b"}
# set1.symmetric_difference_update(set2)
# print(set1)

############## ASSIGNMENT CLASSOWORK : from the given list list1 = [1,2,3,4,5,6,7,8,9,1,2,3,4] print out the new list with no repeated elements.

# list1 = [1,2,3,4,5,6,7,8,9,1,2,3,4]
# sett = set(list1)
# list3 = list(sett)
# print(list3)

############## Print out the no of elements of non repeated elements of the list.

# list1 = [1,2,3,4,5,6,7,8,9,1,2,3,4]
# sett = set(list1)
# list3 = list(sett)
# print(len(list3))


############### HOMEWORK ASSIGNMENT :  list1 = [1,2,3,4,5,6,7,8,9,1,2,3,4] (make the list of those whose duplicate exists.) output : [1,2,3,4]

# list1 = [1,2,3,4,5,6,7,8,9,1,2,3,4]
# list2 = []

# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i] == list1[j] and list1[i] not in list2:
#             list2.append(list1[i])

# print(list2)
    

            


       
