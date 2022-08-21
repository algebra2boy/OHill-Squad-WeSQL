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
    execute_query(db, create_living_area)
    execute_query(db, create_class)
    execute_query(db,create_student)

if __name__ == "__main__":
    main()