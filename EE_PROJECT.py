# Importing a python module for SQL commands
import sqlite3

# Creating a connection between the program and database file
conn=sqlite3.connect('student.db')

# Creating a cursor to execute SQL commands
c=conn.cursor()

# Function to create a table in the file
def CreatingTable():
    c.execute("""CREATE TABLE student (
                first text,
                last text,
                roll integer,
                admin integer,
                cgpa real,
                branch text,
                sem integer
                )""")
    print("\nSuccessfully Created a database file")
    conn.commit()

# Function to insert student data into the file
def InsertingData():
    fn=input("\nEnter your First Name:")
    ln=input("Enter your Last Name:")
    roll=int(input("Enter your Roll number:"))
    admin=int(input("Enter your Admission Number:"))
    cgpa=float(input("Enter your overall CGPA:"))
    branch=input("Enter your Branch:")
    sem=int(input("Enter the Semester you are currently in:"))
    c.execute("INSERT INTO student VALUES (:first,:last,:roll,:admin,:cgpa,:branch,:sem)",{'first':fn,'last':ln,'roll':roll,'admin':admin,'cgpa':cgpa,'branch':branch,'sem':sem})
    conn.commit()

# Function to find details of the student using ROLL number
def RetrievingRoll():
    r=int(input("\nEnter the Roll Number:"))
    c.execute("SELECT * FROM student WHERE roll=:roll",{'roll':r})
    d=c.fetchone()
    print("STUDENT's DETAILS")
    print("First Name: ",d[0])
    print("Last Name: ",d[1])
    print("Roll Number: ",d[2])
    print("Admission Number: ",d[3])
    print("CGPA: ",d[4])
    print("Branch: ",d[5])
    print("Current Semester: ",d[6])

# Function to find details of the student using LAST name
def RetrievingLast():
    l=input("\nEnter the last name:")
    c.execute("SELECT * FROM student WHERE last=:last",{'last':l})
    d=c.fetchone()
    print("STUDENT's DETAILS")
    print("First Name: ",d[0])
    print("Last Name: ",d[1])
    print("Roll Number: ",d[2])
    print("Admission Number: ",d[3])
    print("CGPA: ",d[4])
    print("Branch: ",d[5])
    print("Current Semester: ",d[6])

# Function to find details of the student using ADMIN number
def RetrievingAdmin():
    a=int(input("\nEnter the Admission number:"))
    c.execute("SELECT * FROM student WHERE admin=:admin",{'admin':a})
    d=c.fetchone()
    print("STUDENT's DETAILS")
    print("First Name: ",d[0])
    print("Last Name: ",d[1])
    print("Roll Number: ",d[2])
    print("Admission Number: ",d[3])
    print("CGPA: ",d[4])
    print("Branch: ",d[5])
    print("Current Semester: ",d[6])

#function to find the total number of students
def TotalStudent():
    c.execute("SELECT * FROM student")
    d=c.fetchall()
    print("The total number of student is",len(d))

# Function to delete details of a student through ROLL number
def DeleteStudent():
    a=int(input("\nEnter the roll number of the student to delete :"))
    c.execute("DELETE FROM student WHERE roll=:roll",{'roll':a})
    print("Successfully Deleted the student details from the database")
    conn.commit()
    
# Function to update details of a student using roll number
def UpdateStudent():
    a=int(input("\nEnter the student roll number to update:"))
    cgpa1=float(input("Enter the updated CGPA :"))
    sem1=int(input("Enter the current semester your in:"))
    c.execute("""UPDATE student SET cgpa=:cgpa where roll=:roll""",{'cgpa':cgpa1,'roll':a})
    c.execute("""UPDATE student SET sem=:sem where roll=:roll""",{'sem':sem1,'roll':a})
    print("Successfully Updated the student details")
    conn.commit() 


# Driver code
print("\n\nWELCOME TO STUDENT DATABASE MANAGEMENT SYSTEM!!!!!!")
print("---------------------------------------------------")
print("Select the task you would to perform:\n")
print("1. To Create a student database file")
print("2. To Add the Student Details")
print("3. To Find the Student Details by Roll Number")
print("4. To Find the Student Details by Last Name")
print("5. To Find the Student Details by Admission Number")
print("6. To Find the Total number of Students")
print("7. To Delete the Students Details by Roll Number")
print("8. To Update the Students Details by Roll Number")
print("9. To Exit the program")
a=int(input("Enter your choice between 1-9: "))
if a==1:
    CreatingTable()
elif a==2:
    InsertingData()
elif a==3:
    RetrievingRoll()
elif a==4:
    RetrievingLast()
elif a==5:
    RetrievingAdmin()
elif a==6:
    TotalStudent()
elif a==7:
    DeleteStudent()
elif a==8:
    UpdateStudent()
elif a==9:
    print("Terminating program.......")
    exit()
else:
    print("Please enter a number between 1 - 9")

# To close the connection with the database file
conn.close()