import sqlite3
import datetime
conn = sqlite3.connect("parkinglot.db")
cursor = conn.cursor()


def create_parking():
    cursor.execute(
        """
            create table parking_lot(
                vehicleNum integer primary key autoincrement,
                driverName text not null,
                vehicleType text,
                vehicleWheeler text,
                parkingStartTime text,
                parkingExitTime text,
                totalPrice float
              
                ) 
                """)
    conn.commit()



def insert_parkingdata():
    driverName1 = input("Enter the name of the Driver : ")
    vehicleType1 = input("Enter the Brand of the Vehicle : ")

    startTime = datetime.datetime.now()
    while True:
        print(""" Enter the Vehicle Type :
            1. Two Wheeler
            2. Four Wheeler """)
        vehicle_type_option = int(input("Enter the Vehicle Type : "))

        if(vehicle_type_option == 1):
            vehicleWheeler1 = "Two Wheeler"
            break
        elif(vehicle_type_option == 2):
            vehicleWheeler1 = "Four Wheeler"
            break
        else:
            print("INVALID OPTION CHOOSED")

    cursor.execute("INSERT INTO parking_lot(driverName,vehicleType,vehicleWheeler,parkingStartTime)values(?,?,?,?)",(driverName1,vehicleType1,vehicleWheeler1,startTime))
    conn.commit()

    cursor.execute("SELECT * FROM parking_lot")
    rows = cursor.fetchall() 
    
    filename = input(f"Enter the file name to store slip : ") + ".txt"
    for row in rows:
        with open(filename, mode="w") as file:
            file.write(f"Driver ID: {row[0]}\n")
            file.write(f"Driver Name: {row[1]}\n")
            file.write(f"Car Model: {row[2]}\n")
            file.write(f"Vehicle Wheeler: {row[3]}\n")
            file.write(f"Parked Starting Time: {row[4]}\n")
        
    
    
    
def displayData():
    cursor.execute("SELECT *FROM parking_lot")
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    

def deleteDriver():
    that_id = input("Enter the Driver ID where you want to perform deletion :: ")
    cursor.execute("DELETE FROM parking_lot WHERE id = ? ",that_id)
    conn.commit()
    print(f"SUCESSFULLY Driver ID : {that_id} HAS BEEN DELETED THANK YOU !!!")



def DropParking():
    cursor.execute("DROP TABLE IF EXISTS parking_lot")
    conn.commit()
    print("SUCESSFULLY TABLE HAS BEEN DROPPED THANK YOU !!!")



def exit_park():

    ending_time = datetime.datetime.now()
    a = input("Enter the Vehicle id to identify the EXIT TIME :: ")
    cursor.execute("UPDATE parking_lot SET parkingExitTime = ? WHERE vehicleNum = ? ",(ending_time,a))
    conn.commit()
    
    
    cursor.execute("SELECT parkingStartTime from parking_lot where vehicleNum = ? ",a)
    rows = cursor.fetchall()
    startingtime = rows[0][0]
    format = '%Y-%m-%d  %H:%M:%S.%f'
    start_time = datetime.datetime.strptime(startingtime,format)

    time_interval = ending_time - start_time
    total_hours = time_interval.seconds // 3600  
    total_minutes = (time_interval.seconds % 3600) // 60  
 
    
    cursor.execute("SELECT vehicleWheeler from parking_lot where vehicleNum = ? ",a)
    rows = cursor.fetchall()
    vehicleType = rows[0][0]

    while(vehicleType == "Two Wheeler"):
        print(""" PARKING FAIR FOR TWO WHEELERS :
                  1 HOUR = Rs 10/-
                  AFTER EVERY ADDITIONAL 1 HOUR = Rs 10 + Rs 5/-\n\n """)
        if(total_hours <= 1 and total_minutes == 0):
            total_price = 10
            cursor.execute("UPDATE parking_lot SET totalPrice = ? WHERE vehicleNum = ? ",(total_price,a))
            conn.commit()
            print(f"The Fair of Parking the Vehicle is : Rs {total_price} /- ONLY .......\n\n\n")
            break
        elif(total_hours >= 1 ):
            total_price = 10 + 5 * total_hours

            if(total_minutes > 0):
                total_price += 5
            
            print(f"The fair of parking the Vehicle is : Rs {total_price}/- ONLY .......\n\n\n")
            
            cursor.execute("UPDATE parking_lot SET totalPrice = ? WHERE vehicleNum = ? ",(total_price,a))
            conn.commit()
            break



    
def UpdateParkingData():
    a = input("Enter the Vehicle ID in which you want to perfrom UPDATE :: ")
    b = input(f"Enter the New Driver Name for {a} :: ")
    c = input(f"Enter the New Vehicle Type of Driver No -> {a} :: ")
    while True:
        print(""" Enter the Vehicle Type :
            1. Two Wheeler
            2. Four Wheeler """)
        vehicle_type_option = int(input("Enter the Vehicle Type : "))

        if(vehicle_type_option == 1):
            d = "Two Wheeler"
            break
        elif(vehicle_type_option == 2):
            d = "Four Wheeler"
            break
        else:
            print("INVALID OPTION CHOOSED")
    cursor.execute("UPDATE parking_lot SET driverName = ?,vehicleType = ? ,vehicleWheeler = ? WHERE vehicleNum = ? ",(b,c,d,a))
    conn.commit()

    cursor.execute("SELECT * FROM parking_lot")
    rows = cursor.fetchall() 
    
    filename = input(f"Enter the NEW file name to store slip : ") + ".txt"
    for row in rows:
        with open(filename, mode="w") as file:
            file.write(f"Driver ID: {row[0]}\n")
            file.write(f"Driver Name: {row[1]}\n")
            file.write(f"Car Model: {row[2]}\n")
            file.write(f"Vehicle Wheeler: {row[3]}\n")
            file.write(f"Parked Starting Time: {row[4]}\n")
    
    print("SUCESSFULLY UPDATED !!!!!")
    
   


        

    
