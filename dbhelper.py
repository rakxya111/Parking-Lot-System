
import sqlite3
conn = sqlite3.connect("parkinglot.db")
cursor = conn.cursor()

def create():
    
    cursor.execute(
        """
            create table student(
                id integer primary key autoincrement,
                age integer not null,
                name text 
)
    """ )
    conn.commit()
 
    

def insert():
    age1 = int(input("Enter the age : "))
    name1 = input("Enter the name : ")
    cursor.execute("INSERT INTO student(age,name) values(?,?)",(age1,name1))
    conn.commit()
    
    

def select():
    cursor.execute("SELECT *FROM student")
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    


def update():

    id1 = int(input("Enter the id in which you want to perform update : "))
    age1 = int(input("Enter the age to be updated : "))
    name1 = input("Enter the name to be updated : ")
    cursor.execute("UPDATE student SET age = ? , name = ? WHERE id = ?",(name1,age1,id1))
    conn.commit()
    

def delete():
    that_id = input("Enter the ID where you want to perform deletion : ")
    cursor.execute("DELETE FROM student WHERE id = ? ",that_id)
    conn.commit()
    
    