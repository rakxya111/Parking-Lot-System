########### PYTHON STRINGS

# s = "Hello"
# s[0] = "h" #strings are immutable in python so ERROR will be encountered.
# print(s)


# s = "Hello"
# for i in range(len(s)):
#     if s[i] == "H":
#         b = "hello"
# print(b)


########### concatenating the strings -> to do so the datatype should be same

# s = "hello"
# h = "world"
# print(s + h)


########### METHODS IN PYTHON : 


###########  REPLACING IN PYTHON

########### REPLACING capital h with small h

# name  = "Hello"
# print("Before Refreshing : ",name)
# name = "h" + name[1:]
# print("After Refreshing : ",name)


######### REPLACE METHOD IN PYTHON : SYNTAX : .replace(replace_to,replace_with)

# s = "hello, world!"
# print(s.replace("world","rakshya"))
# print(s)


# s = "hello, world!"
# s = s.replace("hello","hyy")
# print(s)

######## METHOD :
######## .title() -> first letter lai matra capital garna use grne method

# s = "Hello, World!"
# print(s.title())
# print(s.upper())
# print(s.lower())


########## .strip() method -> rstrip() or lstrip()-> agadi ra paxadi ko whitespace haru hataune lai

# s = "    Hello, World!      "
# d = "aaaaaaaaaahellooo"
# print(d.strip("a")) #aba yesle repeated ( a ) chai hatauxa 
# print(s.lstrip()) #left side ko hataune
# print(s.rstrip()) #right side ko hataune
# print(s.strip())

######### converting string to list
# s = "hello world"
# print(list(s))


########## SPLIT METHOD -> .split()

# s = "hello , world"
# print(s.split())

# s = "hello , world"
# print(s.split(",")) # splitting character mentioned i.e. comma chai display hudaena kinaki comma mentioned vako xa bracket vtra

######### JOIN METHOD : 

# list1 = ['hello' , 'world' , '#']
# print(''.join(list1))

# list1 = ['hello' , 'world' , '#']
# print('aabc'.join(list1)) #yo abc chai bich ma join hunxa e.g. hello abc world abc # ani last ma hunna

######## write a program such that given string name2 = "#############hello####world##########" should display output :['hello','world']

name2 = "#############hello####world##########"
org_length = len(name2)
name2 = name2.strip("#")
name1 = name2.split("####")
print(name1) # output : ['hello','world']

############ and then again make that converted output : ['hello','world'] to string name2 = "#############hello####world##########" 


name = "#############hello####world##########"
org_length = len(name)
lside_length = org_length - len(name.lstrip('#'))
rside_length = org_length- len(name.rstrip('#'))
join = '####'. join(name1)
total = "#" * lside_length + join + "#" * rside_length
print(total)

