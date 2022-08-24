import mysql.connector as connector
from mysql.connector import Error
import pandas as pd
from create_and_insert import * 
from query import * 
from update_and_delete import *

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


# Reading data / retrieve Resultset from the database
def read_query(connection, query):
    cursor = connection.cursor()
    resultSet = None
    try:
        cursor.execute(query)
        resultSet = cursor.fetchall()
        return resultSet
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

    # creating a relation
    execute_query(db, create_student_take_class_relation)

    # inserting values into the relation
    execute_query(db, pop_student_take_class)

    print("printing all the students from 'student' table")
    student_result_set = read_query(db, get_all_student_query)
    for result in student_result_set:
        print(result)
    
    # format the resultset with dataframe
    form_db = []

    print("\nprinting students who live in OHill")
    student_OHill_result_set = read_query(db, student_who_live_in_OHILL)
    for result in student_OHill_result_set:
        print(result)
        form_db.append(list(result))
    
    print("\n with prettier layout")
    columns = ['student_id', 'student_name', 'year','Campus_Area', "Building_name"]
    df = pd.DataFrame(form_db, columns=columns)
    print(df)


    # updating the student table 
    execute_query(db, pop_thatcher)
    execute_query(db, update_Yongye_location)
    execute_query(db, update_eric_location)
    student_result_set = read_query(db, get_all_student_query)
    for result in student_result_set:
        print(result)


if __name__ == "__main__":
    main()