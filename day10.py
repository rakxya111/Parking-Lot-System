################# DAY 10 -> PYTHON DICTIONARY

######################################### DICTIONARY (DICT) ##########################################

################# empty_dict = {}

# my_dict = {
#     "name" : "Alice",
#     "age" : 20,
#     "city" : "New York"
# }

# mixed_dict = {
#     1 : "one",
#     "2" : "two",
#     (1,2) : "tuple"
# }

################# accessing the dictionary , we donot use any key in dictionary

# print(my_dict)
# print(my_dict["name"])
# print(mixed_dict[1])
# print(mixed_dict["2"])
# print(mixed_dict[(1,2)])
# print(mixed_dict.get((1,2)))

# print(my_dict["address"]) # error is encountered
# print(mixed_dict.get(("3"))) # none is encountered if element doesnot exist


################# Prints all the keys of the dictionary


# x = mixed_dict.keys()
# print(x)
# print(x[1]) # error 


# car = {
#     "brand" : "ford",
#     "model" : "Muustang",
#     "year" : 1968
# }

# x = car.keys() #only to access the keys of elements of the dict 
# print(x) #before change
# car["colour"] = "pink"
# print(x) #after change
# car["model"] = "mercedes"
# print(car)



################## only to access the values of elements of the dict .values()

# x = car.values()
# print(x)

################## access the keys and values at once using .items() method

# x = car.items()
# print(x)

################### storing the values of the elements in a variable and then accessing using the for loop with .items() method 

# car = {
#     "brand" : "ford",
#     "model" : "Muustang",
#     "year" : 1968
# }

# for k,v in car.items():
#     print("key :",k)
#     print("Value : ",v)


################### updating using .update() method

# car = {
#     "brand" : "ford",
#     "model" : "Muustang",
#     "year" : 1968
# }

# car.update({"year" : 2003})
# print(car)


################### pop -> removes the items with specified key name.

# car = {
#     "brand" : "ford",
#     "model" : "Muustang",
#     "year" : 1968
# }

# car.pop("model")
# print(car)

################### popitem method -> remove the last element that is added

# car.popitem()
# print(car)

################### also can use del keyword (this would delete the set completely)

################### clear method empties the dictionary and return empty dictionary.

# car.clear()
# print(car)

################### SHADOW COPY IN DICT USING  ##################

# car = {
#     "brand" : "ford",
#     "model" : "Muustang",
#     "year" : 1968
# }

# car1 = car # e.g. of shadow copy
# print(car1)
# car.update({"year" : 2003})
# print(car1)

################## DEEP COPY IN DICT 

# car1 = car.copy() # e.g. of deep copy
# print(car1)
# car.update({"year" : 2003})
# print(car1)


################## ANOTHER WAY OF DICT OR NESTED DICT ##################

# myfamily = {
# "child1" : {
# "name" : "rohit",
# "year" : 2003
# },

# "child2" : {
# "name" : "rocky",
# "year" : 2005 
# },

# "child3" : {
# "name" : "rahul",
# "year" : 2008 
# }
# }

# print(myfamily["child1"]["name"])
# myfamily.update({"child1" : { "name" : "sabnam"}}) #update using .update() method
# print(myfamily["child1"]["name"])
# print(myfamily)

# myfamily["child2"]["name"] = "ram" #update
# print(myfamily)

################### access using get method

# print(myfamily.get("child1").get("name"))




################## ASSIGNMENT : FIND THE SUM OF SCORES OF THE STUDENTS AND MAKE SURE THE MORE NO OF STUDENTS ARE ADDED IT WOULD AUTOMATICALLY CALCULATE THE SUM INSTEAD OF DOING IT MANUALLY.
################### OUTPUT :
# student1 score : 10
# student2 score : 35

student = {
"student1" : {
"name" : "rohit",
"score" : [1,2,3,4]

},

"student2" : {
"name" : "rocky",
"score" : [5,6,7,8,9]
}
}

key_name = student.keys()

for k in key_name:
    x = student[k]["score"]
    sum = 0
    for i in x:
        sum += i
    print(f"The sum of score of student {k} is :",sum)


  