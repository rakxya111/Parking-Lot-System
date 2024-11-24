################# FILE HANDLING :
################ fread () reading all the lines one by one character by character.

# f = open("demo.txt","r") # open file in reading mode
# a = f.read() # or print(f.read())
# print(a)
# print(type(a))

# f = open("demo.txt","r") 
# value = f.read()
# print(value[51:66]) # printing good luck
# print(value[-13:]) # printing good luck



"""

read() read character by character.
readline() read one line at a time,also read one line at a time and inserts it into a string
readlines() read all the lines at once,read all the line at a time (fetch all) for large files and then inserts it into the list


"""
################ NOTE : Do close the file in the end unless you don't want the file to be corrupt

# f = open("demo.txt","r") 
# a = f.readlines()
# print(a[4]) 
# print(f.readline()) # read only one line at a time.

# f = open("demo.txt","r") 
# print(f.readlines()) # read all the lines and put it into the list.

################ for printing the type of each line of the text file.

# f = open("demo.txt","r") 
# val = f.readlines()
# for i in val:
#     print(type(i))
#     print(i)



##################### IF we are working on non-CSV file then we can write down the code like this.
##################### This code would read each and every data of csv file and then put it into the list by removing the \n new line as well.


# f = open("data.csv","r")
# lst = []

# for i in f:
#     val = i.strip("\n").split(",")
#     lst.extend(val)

# print(lst)



################ NOTE : Whenever we are working on CSV file then we better (import the csv) and write down the csv code just as we have done down in here.

################ READ CSV FILE :

# import csv

# with open("data.csv",mode="r") as file:
#     csv_reader = csv.reader(file) # read the csv file
#     header = next(csv_reader) # start reading from next line by skipping (line skip out)

#     for x in csv_reader:
#         print(x)


    

############## WRITE INTO CSV FILE :
  
############## This code is to write onto a CSV file :

#  OR # file_path = "output.csv" 

# data = [
#     ['Alice',30,'London'],
#     ['Bob',25,'Paris'],
#     ['Charlie',45,'Berlin']
# ]

# with open("output.csv",mode="w",newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Name','Age','City']) # write into the empty csv file.
    
#     for i in data:
#         csv_writer.writerow(i) # write all the above provided data into the csv file.



############## Delete a File : To delete a file, you must import the OS module, and run its os.remove() function


# import os
# os.remove("demofile.txt") # Now after running this the demofile.txt has been removed



############## CHECK IF FILE EXISTS : To avoid getting an error, you might want to check if the file exists before you try to delete it:


# import os

# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
# else:
#     print("FILE DOESNOT EXISTS.")



############## Delete Folder : To delete an entire folder, use the os.rmdir() method:

# import os
# os.rmdir("foldername")
