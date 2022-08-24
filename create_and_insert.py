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
    class_id integer,
    professor_name varchar(255),
    class_name varchar(255),
    department varchar(20),
    primary key (department, class_id)
);
"""



create_student = """
create table student(
    student_id integer primary key,
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
INSERT INTO student (student_id, name, year, campus_Area, building_name) Values
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
INSERT INTO class (department, class_id, class_name, professor_name) VALUES
("CS", 345 , "Practice and Applications of Data Management", "Jaime Davila"),
("CS", 220 , "Programming Methologies", "Marius Minea "),
("CS", 230 , "Computer Systems Principles", "Meng-Chieh Chiu"),
("CS", 240 , "Reasoning under Uncertainty", "Andrew Lan"),
("CS", 250 , "Introductio to Computation", "David Barrington"),
("CS", 311, "Introduction to Algorithms", "Marius Minea"),
("Math", 235, "Linear Algebra", "TBA"),
("Math", 331, "Ordinary Differential Equations", "Garrett Cahill")
"""

create_student_take_class_relation = """
create table student_takes_class (
    year integer,
    student_id integer,
    class_id integer,
    department varchar(20),
    foreign key (student_id) references student (student_id),
    foreign key (department, class_id) references class (department, class_id),
    primary key (department, class_id, student_id, year) ); 
"""

pop_student_take_class = """
Insert into student_takes_class (department, class_id, student_id, year) values
("CS", 230 ,3,2021),
("CS", 230 ,6,2021),
("CS", 230 ,7,2021),
("CS", 230 ,1,2022),
("Math", 235, 1, 2022),
("CS", 240, 1, 2022),
("CS", 311, 4, 2022),
("CS", 311, 2, 2022),
("CS", 311, 3, 2022),
("CS", 240, 7, 2020)

"""

pop_thatcher = """
INSERT INTO living_area (campus_Area, building_name, Honor) VALUES
("Northeast", "Thatcher", 0)
"""