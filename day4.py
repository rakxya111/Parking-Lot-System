############### ITERATION IN PYTHON
'''
Iteration refers to the process of repetedly executing the block of code.
For loop : list , tuple , string or range lai iterate grna ko lagii.
While loop : executes a block of code as long as the condition is true.
Do -while : COndition checks later

'''
################ EXAMPLES:

# numbers = [1,2,3,4,5]
# for num in numbers: #in matlab euta euta number in numbers print gara vannu ho
#     print(num)


################ PRINITNG if the number is 3

# numbers = [1,2,3,4,5]
# for num in numbers:
#     if num == 3:
#         print(num)
#     else:
#         print("Its not three.")


################ PRINTING ONLY ODD

# numbers = [1,2,3,4,5]

# for n in numbers:
#     if n % 2 != 0:
#         print(n)
#     else:
#         print(f"{n} is not odd number.")


################ LOOPING THROUGH STRING

# # for x in "banana":
# #     print(x)


################ NO OF n in banana

# fruit = "banana"
# count = 0
# for x in fruit:
#     if x == 'n': #can also use is(identity operator)
#         count += 1

# print("The no of n in BANANA is ",count)



################ BREAK IN PYTHON : exit the loop if the break statement is true

# fruits = ['apple','banana','cat']

# for x in fruits:
#     print(x)
#     if x == 'banana':
#         break


# for x in "banana":
#     print(x)
#     if x == 'n':
#         print("before break")
#         break
#     print("after break")

 
 

################ CONTINUE IN PYTHON : SKIP THE CURRENT ITERATION OF the loop if the CONTINUE statement is true

# fruits = ['apple','banana','cat']

# for x in fruits:
#     if x == 'banana':
#         continue
#     print(x)


################ CONTINUE AND BREAK IN ONE

# num = [1,2,3,4,5,6,7,8,9,10]

# for x in num:
#     if x == 5:
#         continue
#     elif x == 7:
#         break
#     print(x)

############### RANGE : 0 bata start hunxa

# for x in range(20):
#     print(x)

# mul = 1
# for x in range(6):
#     if x == 0:
#         continue
#     else:
#         mul *= x

# print("The multiplication from 1 - 6 is : ",mul)



################ SPECIFYING THE RANGE start and end

# for x in range(2,8):
#     print(x)

# for x in range(-100,2):
#     print(x)

# for x in range(2,30,2):
#     print(x)



################ even print with range with extra parameter

# for x in range(0,30,2): #euta euta skip hunxa
#     print(x)

################ odd print with range with extra parameter
# for x in range(1,30,2):
#     print(x)


################ INNER LOOP

# adj = ['red','blue','yellow','green']
# fruits = ['apple','banana','cherry']

# for x in adj:   
#     for y in fruits:
#         print(x,y)

# num1 = [5,6,7]
# num2 = [1,2,3,4,5,6,7,8,9,10]

# for i in num1:
#     print(f"The table of {i} is :")
#     for j in num2:
#         print(f"{i} * {j} =",i*j)
        


