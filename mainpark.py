import parkhelper
import time
from parkhelper import create_parking, insert_parkingdata,displayData,deleteDriver,DropParking,exit_park,UpdateParkingData

data = 0
while True:
  
    data = int(input("""PLEASE SELCET THE OPERATION \n 
    || Press 1 CREATE THE PARKING TABLE\n 
    || Press 2 INSERT INTO THE PARKING TABLE \n 
    || Press 3 DISPLAY PARKING DATA \n 
    || Press 4 DELETE THE DATA IN PARKING LOT \n 
    || Press 5 DROP THE PARKING TABLE DATA  \n 
    || Press 6 TOTAL PARKING FAIR AND EXIT TIME \n 
    || Press 7 UPDATE PARKING DATA \n 
    || Press 8 EXITTTT \n\n Enter the option now :: """))

    if (data == 1):
        create_parking()
    elif(data == 2):
        insert_parkingdata()
    elif(data == 3):
        displayData()
    elif(data == 4):
        deleteDriver()
    elif(data == 5):
        DropParking()
    elif(data == 6):
        exit_park()
    elif(data == 7):
        UpdateParkingData()
    elif(data == 8):
        print("EXIT SUCESSFULLY !!!!")
        break

        
    

        


   

    

    