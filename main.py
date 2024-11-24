
import dbhelper

while True:
    input_data = int(input("Enter the opeartion You want to perform in database \n 1. CREATE TABLE \n 2. INSERT DATA INTO TABLE \n 3. READ OPERATION \n 4. UPDATE OPEARTION \n 5. DELETE OPERATION \n 6. EXIT \n:: "))

    if (input_data == 1):
        from dbhelper import create 
        create()
    elif(input_data == 2):
        from dbhelper import insert 
        insert()
        
    elif(input_data == 3):
        from dbhelper import select 
        select()
    elif(input_data == 4):
        from dbhelper import update
        update()
    elif(input_data == 5):
        from dbhelper import delete 
        delete()
    elif(input_data == 6):
        break
    else:
        print("Please select the right input data.")
