"""

PostgreSQL CRUD Using SQLAlchemy ORM (Single File)


This file demonstrates CRUD Operations using
SQLAlchemy ORM and PostgreSQL.

Everything is written inside one file.

Topics:
1. Database Connection
2. Student Model
3. Create Table
4. CRUD Operations
5. Menu
"""



# Imports


from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# Database URL

DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/student_crud_db"

# Create Engine

engine = create_engine(DATABASE_URL)


# Base Class

Base = declarative_base()



# Student Model

class Student(Base):

    __tablename__ = "studentcrud"

    student_id = Column(Integer, primary_key=True)

    name = Column(String(100))

    roll_number = Column(String(20), unique=True)

    email = Column(String(100), unique=True)

    department = Column(String(100))

    semester = Column(Integer)

    cgpa = Column(Float)



# Create Table

Base.metadata.create_all(bind=engine)



# Session Factory

SessionLocal = sessionmaker(
    bind=engine
)



# Create Student

def create_student():

    session = SessionLocal()

    name = input("Enter Name: ")
    roll_number = input("Enter Roll Number: ")
    email = input("Enter Email: ")
    department = input("Enter Department: ")
    semester = int(input("Enter Semester: "))
    cgpa = float(input("Enter CGPA: "))

    new_student = Student(

        name=name,
        roll_number=roll_number,
        email=email,
        department=department,
        semester=semester,
        cgpa=cgpa

    )

    session.add(new_student)

    session.commit()

    print("Student added successfully.")

    session.close()



# View Students

def view_students():

    session = SessionLocal()

    students = session.query(Student).all()

    if not students:

        print("No students found.")

    else:

        for student in students:

            print("Student ID :", student.student_id)
            print("Name       :", student.name)
            print("Roll No    :", student.roll_number)
            print("Email      :", student.email)
            print("Department :", student.department)
            print("Semester   :", student.semester)
            print("CGPA       :", student.cgpa)

    session.close()

# Update Student

def update_student():

    session = SessionLocal()

    student_id = int(input("Enter Student ID: "))

    student = session.query(Student).filter_by(
        student_id=student_id
    ).first()

    if student:

        student.name = input("Enter Name: ")
        student.roll_number = input("Enter Roll Number: ")
        student.email = input("Enter Email: ")
        student.department = input("Enter Department: ")
        student.semester = int(input("Enter Semester: "))
        student.cgpa = float(input("Enter CGPA: "))

        session.commit()

        print("Student updated successfully.")

    else:

        print("Student not found.")

    session.close()



# Delete Student

def delete_student():

    session = SessionLocal()

    student_id = int(input("Enter Student ID to delete: "))

    student = session.query(Student).filter_by(
        student_id=student_id
    ).first()

    if student:

        session.delete(student)

        session.commit()

        print("Student deleted successfully.")

    else:

        print("Student not found.")

    session.close()

# Main Menu

while True:

    print("1. Create Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        create_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        update_student()

    elif choice == "4":

        delete_student()

    elif choice == "5":

        print("Program Closed Successfully.")
        break

    else:

        print("Invalid Choice. Please try again.")