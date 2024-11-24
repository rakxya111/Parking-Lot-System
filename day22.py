############################### PANDAS REMOVING DUPLICATES #########################################
####################################################################################################


# import pandas as pd
# data = {
#         'Name' : ['alice','alice','charli',None,'barli','ram','hari',None,'januka','vivek'],
#         "Age" : [25,25,20,44,23,20,10,None,55,78],
#         "city" : ['NewYork','NewYork','Chichago',None,'KTM',None,'BKT','Patan','Tinkune','Suryabinayak'],
#         "Date" : ["2020/12/10","2020/12/10","2019/12/01","2000/12/01","2010/12/01","2011/12/01","2022/12/01","2003/12/01","2004/12/01","20051201"]
#         }

# df = pd.DataFrame(data)
# df.drop_duplicates(inplace = True) # NOTE : with inplace the data are modified in the dataframe.
# print(df)

# NOTE : if (inplace) isnot included the data is modified in the run time only.


################ Matplotlib is actually used for plotting the graph purposes but the POWER BI is the best for plotting graph (Matplotlib is a low level graph plotting library in python that serves as a visualization utility.)


# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,3,5,7,11]

# plt.plot(x,y, marker = "o",linestyle = "--",color = "b",label = "Prime Numbers") # Here even a minor mistake can affect alot and the program might not run soo we need to check properly 
# plt.xlabel('X Axis') # labeling the x axis segment in graph as x-axis
# plt.ylabel('Y Axis') # labeling the y axis segment in graph as y-axis
# plt.title("Prime Numbers Plot") 
# plt.legend() 
# plt.show()  # TO Display the plot



import matplotlib.pyplot as plt
import numpy as np
xpoint = np.array([45,56])
ypoint = np.array([467,563])

plt.plot(xpoint,ypoint,'o:r', ms=20) # NOTE : r is red ,o is marker, (:) is used for joining line , ms = marker size , msr = border of the marker , FORMAT : marker|line|color
plt.grid()  # Display the graph in grid format
plt.show()