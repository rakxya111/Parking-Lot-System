# matrix = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ]

# for x in matrix:
#     print(x)
#     print(type(x))

########## if data position known then use this to access matrix 
########## best way to access the matrix
 
# print(matrix[0]) 
# print(matrix[0][1])
 

####### if data position is NOT known then use this to access matrix 

# matrix = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ]

# for row in matrix:
#     for elements in row:
#         print(elements,end = ' ')
#     print()

########## list = mutable and tuple = immutable and faster

########## MEMBERSHIP OPERATOR : in , not in

# fruits = ["apple","banana","strawberry"]
# print("apple" in fruits)
# print("dog" in fruits)
# print("a" in "apple")
# print("d" not in "apple")

############ INSERT METHOD -> .insert(index,value_to_insert)

# fruits = ["apple","banana","strawberry"]
# fruits.insert(1,"orange")
# fruits.insert(100,"catt")
# fruits.insert(-1,"dog")
# fruits.insert(2,"dog")
# print(fruits)


############ EXTEND METHOD -> .extend(to_extend_list) -> extended the list fruits with the list of vegetables (see eg down)

# fruits = ["apple","banana","strawberry"]
# vegetable = ['potato','tomato','carrot']
# fruits.extend(vegetable)
# print(fruits)


############ EXTENDING TUPLE TO LIST

# this_list = ["apple","banana","strawberry"]
# this_tuple = ("kiwi","orange")
# this_list.extend(this_tuple)
# print(this_list)


############ EXTENDING SET TO LIST

# this_list = ["apple","banana","strawberry"]
# this_set = {"kiwi","orange"}
# this_list.extend(this_set)
# print(this_list)

############ REMOVE IN LIST -> only remove the first occurence in the list [We would use this If we want to remove on the basis of data]

# this_list = ["apple","banana","strawberry"]
# this_list.remove("apple")
# print(this_list)

############ POP IN LIST -> only remove the first occurence in the list [If we want to remove on the basis of index position][index position not given then last element is removed ]

# this_list = ["apple","banana","strawberry"]
# this_list.pop(2)
# this_list.pop(100) #error
# print(this_list)

############# Del keyword :- also delete list completely

# this_list = ["apple","banana","strawberry"]
# del this_list
# print(this_list)

############## Clear method empties the list (only the content and give empty list)

# this_list = ["apple","banana","strawberry"]
# this_list.clear()
# print(this_list)

############## SORT method -> will sort list alphanumerically,ascending by default.


# this_list = ["zebra","orange","apple","banana","strawberry"]
# this_list1 = [100,2,4,1,5,6]
# this_list.sort() #also index position is changed when sorted
# this_list1.sort()
# print(this_list)
# print(this_list1)

############## SORT IN DESCENDING ORDER IN LIST -> this is case insensitive.

# this_list = ["zebra","orange","apple","banana","strawberry"]
# this_list1 = [100,2,4,1,5,6]
# this_list.sort(reverse = True) #also index position is changed when sorted
# this_list1.sort(reverse = True)
# print(this_list)
# print(this_list1)

############### SORT in lowercase -> so yeta chai aba lowercase paila priority dine yestaii keii hunxa.

# this_list = ["zebra","orange","Zebra","Orange","Apple"]
# this_list.sort()
# print(this_list)
# this_list.sort(key = str.lower)
# print(this_list)


################ REVERSE METHOD -> reverses the current sorting of elements (paxhadi bata print hunxa not alphanumerically or something.)

# this_list = ["zebra","orange","apple","banana","strawberry"]
# this_list.reverse()
# print(this_list)

############## DEEP COPY : copy using .copy() method
# COPY METHOD IN LIST : naya face banako jstai ho .copy() method vaneko

# this_list = ["zebra","orange","apple","banana","strawberry"]
# new_list = this_list.copy()
# this_list.append("mango") # new update won't be affected to new list ,won't be appended in the list
# print(new_list)


############## SHADOW COPY : NOT using .copy() method

# this_list = ["zebra","orange","apple","banana","strawberry"]
# new_list = this_list # new update will be affected to new list ,will be appended in the list
# this_list.append("mango")
# print(new_list)


############### APPEND USING + OPERATOR : 

# list1 = [1,2,3,4,5]
# list2 = ["a","b","c","d"]
# list4 = ["z","x","e","m"]

# list3 = list1 + list2 + list4
# print(list3)


#################  LIST COMPREHENSION : appending the selected items from the list such as copying only those whose character is "a" and so-on. 

# fruits = ["apple","banana","strawberry"]
# newlist = []

# for x in fruits:
#     if "p" in x:
#         newlist.append(x)
# print(newlist)

################## SHORTED FORM OF LIST COMPREHENSION 

# num = [1,2,3,44,5,5,66,7]
# newlist = [x for x in num if x % 2 == 0]
# print(newlist)

# fruits = ["mango","apple","banana","carrot"]
# new_fruits =[value for value in fruits if "o" in value]
# print(new_fruits)



################### SORTED METHOD ->  using .sorted() -> it will make new list after sorting (naya list ma update garna pryo vane yo use garne navaye sort matra use garne)

# this_list = ["zebra","orange","apple","banana","strawberry"]
# new_list = sorted(this_list)
# print(this_list)
# print(new_list)

########################################## TUPLE #################################################### 



#################### Tuple can't be modified , delete or update , so if we want to do sooo first convert it to the list.

# tup = (1,2,3,4,5)
# print(tup[1]) #can be accessed using index position , can be use range or slice
# x = list(tup)
# print(type(x))


#################### Unpacking a tuple -> xuta xutai variable ma items of list laiii rakhne

# fruits = ("apple","bananna","cherry")
# (green,yellow,orange) = fruits
# print(green)
# print(yellow)
# print(orange)

################### ASSIGNMENT 1 : SHORTED FORM OF LIST COMPREHENSION ###################

# fruits = ["mango","apple","banana","carrot"]
# new_fruits =[value for value in fruits if "o" in value]
# print(new_fruits)

################### ASSIGNMENT 2 : Calculate the sum of all the elements in a matrix using nested loops: 


# matrix = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ]

# sum = 0 
# for row in matrix:
#     for elements in row:
#         sum += elements

# print("The sum of the elements in the matrix is : ",sum)        

      
        



