############## WHILE LOOP IN PYTHON

############## BREAK IN WHILE LOOP
# i = 1

# while i < 8:
#     print(i)
#     if i == 3:
#         break
#     i += 1 


################ INFINITELY RUNS THE LOOP
# i = 1

# while i < 8:
#     print(i)
#     if i == 3:
#         continue
#     i += 1 


################ CONTINUE IN WHILE LOOP

# i = 1

# while i < 8:
#     if i == 3:
#         continue
#     print(i)
#     i += 1 


################ SWAPPING IN VARIABLE IN PYTHON


#  # (FIRST WAY)
# x , y = 10 ,100
# x , y = y , x
# print(x,y)


# ############### (SECOND WAY)

# x , y = 10 , 20 
# print(f"BEFORE SWAPPING : The x is now {x} and y is now {y}.",x,y)
# temp = x
# x = y
# y = temp
# print(f" AFTER SWAPPING : The x is now {x} and y is now {y}.",x,y)


################ SWAPPIING WITHOUT TEMP (IMP ASKED IN INTERVIEW) (THIRD WAY)

# x , y = 10, 20
# print(x,y)
# x = x + y # x = 30
# y = x - y # y = 10
# x = x - y # x = 20
# print(x,y)



############### PYTHON STRINGS -> fundamental datatype used to represent text .( It is immutable )-> Can't be update or delete (means can't modify)
# We have single Line strings and multiple line strings in python


############## SINGLE LINE STRING

# name = 'hello " world '
# print(name)


################ MULTIPLE LINE STRING

# multiline_string = '''
# This is a multiple line string 
# You can write the text over multiple line '''
# print(multiline_string)

################ DOC STRING

# """
# This is a doc string or used to probably used to write multiple line comments.

# """


################ INDEXING IN PYTHON -> alwyz starts with index 0

# s = "hello , world"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# print(s[6])
# print(s[10])
# print(s[-1]) # matlab at the end bata suru hunxa e.g. yesma aba d print hunxa
# print(s[-2])
# # print(s[100]) #ERRORR 

############### SLICING -> SYNTAX : s[start:stop:step] step 1 vayo vane skip hudaena , step 2 vayo vane euta skip hunxa ani yedi step chai 3 vayo vane 2 ta skip hunxa and so-on. Yedi step ko thau ma -1 rakhyo vane reversal way ma print hunxa.

# s = "hello, World!"
# print(s[0:5])
# print(s[7:12])
# print(s[-13:12])
# print(s[-11:12])
# print(s[-6:-1]) 

# s = "hello, World!"
# print(s[:5]) # 5th vanda agadi ko sav nikalnu xa vane yo use garne aba kinaki lets assume that, starting tha vayena vane we could just keep it empty and pachadi ko mtra rakhxau
# print(s[5:]) 

# print(s[:-8])

# s = "hello, World!"
# print(s[::2]) #start postion pani thaxaina(not mentioned) end ni thaxaina(not mentioned) ani euta skip grdai print hunxa
# print(s[::3]) #duita skip hunxa


# s = "hello, World!"
# print(s[::-1]) #reverse print hunxa yesbata without using the method




############### METHODS IN PYTHON
############### len() : starts with 1 while index starts with 0

# s = "hello, World!"
# print(len(s))


############### INDEX postion using range with len() method
# s = "Hello, World!"

# for i in range(len(s)):
#     print(f"Character at index {i} is {s[i]}.")

################ INDEX OF ONLY w of above string

# s = "Hello, World!"

# for i in range(len(s)):
#     if s[i] == 'W':
#         print(f"The postion of  W is : ",i)


################ USING METHOD LOWER : syntax : lower()

# s = "Hello, World!"

# for i in s:
#     if i.lower() == 'h':
#         print("The character is h or H")
#         print(i) #output : H (capital h) because string is immutable
#     else:
#         print(f"The character is {i} not h or H.")

