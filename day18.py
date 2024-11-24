############## GET THE CURRENT WORKING DIRECTORY :

# import os
# current_dir = os.getcwd() ## get current working directory
# print(current_dir)

################# list files in the current directory 
################# used to search the files and perform manipulation

# import os
# files = os.listdir(current_dir)
# print(files)

################ GET random number from the list :

# import  random
# random_number = random.randint(1,10)
# print(random_number)

################ shuffle a list :

# import  random
# my_list = [1,2,3,4,5,8,9,20]
# random.shuffle(my_list)
# print(my_list)

############### PERFORM MATHEMATICAL OPERATIONS :

# import math
# sqrt_value = math.sqrt(25)
# print(sqrt_value)

# factorial_value = math.factorial(5)
# print(factorial_value)





#####################################################################################################
############################# WORKING WITH DATABASE IN PYTHON #######################################
#####################################################################################################



########## NOTE : FIRST DOWNLOAD SQLITE AND SQLITE3 EDITOR AND THEN IMPORT SQLITE3 AND THEN CREATE CONNECTION TO DATABASE AND SOON

# import sqlite3

# conn = sqlite3.connect("test.db") # connect to a database or create a new one if doesnot exist
# cursor = conn.cursor()

# cursor.execute("SHOW DATABASES")


################## CREATING THE TABLE IN THE DATABASE :

# cursor.execute( 
#     '''
#                 Create table if not exists users(
#                 id integer primary key,
#                 username text not null,
#                 age integer,
#                 email text unique
#                 )

# '''
# )

############ NOTE : DONOT forget to COMMIT once you have make changes into the database unless you are retriving

############# INSERTING INTO TABLE : 

# cursor.execute("insert into users (id,username,age,email) values (1,'alice',30,'alice@gmail.com'),(2,'hello',30,'hello@gmail.com')")
# conn.commit()


############## inserting muliple data into the database table in the form of list : #############

# users = [
#     ('bob',25,'bob@gmail.com'),
#     ('charlie',20,'charlie@example.com')
# ]

# cursor.executemany("insert into users (username,age,email) values (?,?,?)",users)
# conn.commit() # commiting is important once you have made changes


############# RETRIEVE THE DATA FROM THE DATABASE TABLE : (MUSTNOT COMMIT CAUSE JUST RETRIEVING)

# cursor.execute("select *from users")
# rows = cursor.fetchall()
# print("all records")
# for i in rows:
#     print(i)

############# UPDATING THE DATA IN THE DATABASE TABLE : (MUST COMMIT)

# cursor.execute("update users set age = 31 where username = 'alice'")
# conn.commit()

############# DELETING THE DATA FROM THE DATABASE TABLE : (MUST COMMIT)

# cursor.execute("delete from users where username = 'bob'")
# conn.commit()


##############################################################################
############################ ASSIGNMENT : ####################################

# data to be written into the csv file
# data = [
#     ['Alice',30,'London'],
#     ['Bob',25,'Paris'],
#     ['Charlie',45,'Berlin'],
#     ['Mandy',56,'Tokyo'],
#     ['Sarita',67,'Kathmandu'],
#     ['JianJian',26,'China'],
#     ['Wunsav',30,'Korea'],
#     ['Rakshya',21,'Nepal'],
#     ['Hridayandra',23,'NYC'],
#     ['Sanjok',36,'Virginia'],
#     ['Ganesh',88,'Melborne'],
#     ['Kanchan',22,'Australia']
# ]

# # writing the above data into the csv file
# import csv
# with open("value.csv",mode = "w",newline="") as file:
#     csv_writer = csv.writer(file)
    
#     for i in data:
#         csv_writer.writerow(i)



# import sqlite3
# conn = sqlite3.connect("data.db") # creating connection in the database "data.db"
# cursor = conn.cursor()

# # creating the table (data) in the data.db (database)
# cursor.execute(
# '''
#      create table if not exists data(
#         name text not null,
#         age integer,
#         address text not null
# )
# '''
# )


# # retrieving all the data from value.csv file and then appending all that data into the list named (data)
# data = []
# with open("value.csv",mode="r")as file:
#     csv_reader = csv.reader(file)
#     for i in csv_reader:
#         data.append(i)

# # Now inserting all the data from the list named data to the database table in the database
# cursor.executemany("insert into data (name , age , address) values (?,?,?)",data)
# conn.commit() # commiting the changes

# # retrieving all the data from the database table and then fetching all and displaying it in the terminal
# cursor.execute("select *from data")
# rows = cursor.fetchall()
# print("ALL RECORDS:")
# for i in rows:
#     print(i)


#################### RANDOM IN PHP EXAMPLE : #############################

import random
data = ['oggy','doraemon','nobita','shizuka','suneo','jian','hatori','kenechi','shishumano']
final = []
for _ in range(len(data)):
    random_name = random.choice(data)
    random_age = random.randint(1,11)
    random_email = random_name.lower() + f"{random_age}" + "@gmail.com" 
    final.append((random_name,random_age,random_email))

print(final)

import csv
with open("file.csv",mode='w')as file:
    write_data = csv.writer(file)

    for i in final:
        write_data.writerow(i)
