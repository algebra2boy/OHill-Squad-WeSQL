import mysql.connector as connector
from mysql.connector import Error
import pandas as pd

create_database_query = "CREATE DATABASE OHILL;"
create_living_area = """
Create table living_area (
    campus_Area varchar(30),
    building_name varchar(30),
    Honor BIT(1),
    primary key (campus_Area, building_name)
);
"""

create_class = """
create table class(
    id integer,
    professor_name varchar(255),
    class_name varchar(255),
    department varchar(20),
    primary key (department, id)
);
"""

create_student = """
create table student(
    id integer primary key,
    name varchar(30),
    year integer,
    campus_Area varchar(30),
    building_name varchar(30),
    foreign key (campus_Area, building_name) references living_area (campus_Area, building_name)
);

"""
pop_living_area = """
INSERT INTO living_area (campus_Area, building_name, Honor) VALUES
("OHill", "Webster", 0),
("OHill", "Grayson", 0),
("OHill", "Field", 0),
("Commonwealth", "Elm", 1),
("Northeast", "Crabtree", 0),
("Central", "Brook", 0)
"""


pop_Students = """
INSERT INTO student (id, name, year, campus_Area, building_name) Values
(1, "Yongye", 2, "OHill", "Webster"),
(2, "Anan", 3, "Commonwealth", "Elm"),
(3, "Jeff", 3, "OHill", "Grayson"),
(4, "Matt", 3, "OHill", "Field"),
(5, "Tina", 2, "Northeast", "Crabtree"),
(6, "Adam", 3, "OHill", "Grayson"),
(7, "Eric", 4, "Central", "Brook"),
(8, "Navid", 4, "OHill", "Grayson")
"""

pop_Class = """
INSERT INTO class (department, id, class_name, professor_name) VALUES
("CS", 345 , "Practice and Applications of Data Management", "Jaime Davila"),
("CS", 220 , "Programming Methologies", "Marius Minea "),
("CS", 230 , "Computer Systems Principles", "Meng-Chieh Chiu"),
("CS", 240 , "Reasoning under Uncertainty", "Andrew Lan"),
("CS", 250 , "Introductio to Computation", "David Barrington"),
("CS", 311, "Introduction to Algorithms", "Marius Minea"),
("Math", 235, "Linear Algebra", "TBA"),
("Math", 331, "Ordinary Differential Equations", "Garrett Cahill")
"""


def create_server_connection(host_name: str, user_name: str, user_password: str):
    connection = None
    # the try-except clause is to prevent the conenction is failed
    try:
        connection = connector.connect(host=host_name,
             user=user_name, 
             password=user_password, 
             port=3306)
        print("MySQL Database connection successfully")
    except Error as error:
        print(f"error is {error}")
    return connection

def create_database(connection, sql_query):
    cursor = connection.cursor()
    try: 
        cursor.execute(sql_query)
        print("Database  successfully")
    except Error:
        raise Error("Database already exists")

def create_db_connection(host_name: str, user_name: str, user_password: str, Database: str):
    connection = None
    # the try-except clause is to prevent the conenction is failed
    try:
        connection = connector.connect(host=host_name,
             user=user_name, 
             password=user_password, 
             port=3306,
             database=Database)
        print(f"MySQL Database {Database} connection successfully")
    except Error as error:
        print(f"error is {error}")
    return connection

# this function creates a potential error, which is SQL injection
def execute_query(connection, query):
    cursor = connection.cursor()
    try: 
        cursor.execute(query)
        connection.commit()
        print("Query execution successfully")
    except Error as err:
        print(f"Error: '{err}")

def main():
    # this connection is used to connect to the mySQL 
    connection = create_server_connection("127.0.0.1", "root", "root12ab")
    try:
        create_database(connection, create_database_query)
    except Error as err: 
        print(err)
    # this connection is used to connect to the mySQL database/schema
    db = create_db_connection("127.0.0.1", "root", "root12ab", 'OHILL')

    # creating the tables
    execute_query(db, create_living_area)
    execute_query(db, create_class)
    execute_query(db, create_student)
    
    # inserting values into the tables 
    execute_query(db, pop_living_area)
    execute_query(db, pop_Students)
    execute_query(db, pop_Class)

    

if __name__ == "__main__":
    main()