############################################# PANDAS IN PYTHON :#####################################
######################################################################################################
######################################################################################################

# NOTE : -> Pandas allows us to analyze big data and make conclusions based on statistical theories.                     
# NOTE : -> Pandas can clean messy data sets, and make them readable and relevant.


# import pandas as pd
# data = {
# "Name" : ['alice','bob','charli'],
# "Age" : [25,30,20],
# "city" : ['NewYork','LA','Chichago']
# }
# df = pd.DataFrame(data) # inserting the above datas into a data frame(Means like insertig in table format)
# print(df)


##################### Reading the CSV file into a DataFrame

# import pandas as pd
# df = pd.read_csv("file.csv")
# print(df.head()) # head() method will return the top 5 rows.
# df.to_csv('file.csv',index=False) # writing dataframe to csv file without any index number in it
# df.to_csv('file.csv') 

#################### Dataframe with the age that is greater than 25

# filtered_df = df[df['Age'] > 25] 
# print(filtered_df)


#################### Creating a column IsAdult in the DataFrame where tha age is greater than 30

# df['IsAdult'] = df['Age'] > 30
# print(df.head())

################### removing a column city 

# df.drop(columns = ['city'] , inplace=True) 
# print(df)

################### removing a column city without adding inplace but in this we must assign a variable to do so

# a = df.drop(columns = ['city'] ) 
# print(a)

################### Sorting the data on the basis of the age parameter

# sorted_df = df.sort_values(['age'])


import pandas as pd
data = {
        'Name' : ['alice','bob','charli',None,'barli','ram','hari',None,'januka','vivek'],
        "Age" : [25,30,20,44,23,20,10,None,55,78],
        "city" : ['NewYork','LA','Chichago',None,'KTM',None,'BKT','Patan','Tinkune','Suryabinayak'],
        "Date" : ["2020/12/10","2020/12/01","2019/12/01","2000/12/01","2010/12/01","2011/12/01","2022/12/01","2003/12/01","2004/12/01","20051201"]
        }

# df = pd.DataFrame(data)
# print(df)

# new_df = df.dropna() ###### drop those whose value is NONE 


####### In age column in dataframe wherever there is None replace it with 130

# age = df['Age']
# age.fillna(130,inplace=True) # In place of None in age replace it with 130
# print(df)

######### IN THIS The date in the dataframe written out in proper format "ISO8601" as in above in last the date is written messy

# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'],format = "ISO8601")
# print(df.to_string())

######### IN row 7 in age replace with 111

# df = pd.DataFrame(data)
# df.loc[7,'Age'] = 111 
# print(df)


######## In age column in DF wherever the age is greater than 40 replace it witj 222

# df = pd.DataFrame(data)
# for x in df.index:
#     if df.loc[x,'Age'] > 40:
#         df.loc[x,'Age'] = 222

# print(df)


######## DELETEING THOSE age in 7th row in the DF where the age is greater than 40

# df = pd.DataFrame(data)
# for x in df.index:
#     if df.loc[x,'Age'] > 40:
#         df.drop(x ,inplace = True)
# print(df)