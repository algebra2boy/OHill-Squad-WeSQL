## What this is about
I took CS 345, which is about Database Management, and the class did not teach us much about how to connect the database with Python or other major languages. 
I wanted to learn how to create and manipulate SQL databases with Python through this personal project.

## Important downloads
1. [mySQL Community Server](https://dev.mysql.com/downloads/mysql/)
    - must be downloaded first to connect the mySQL server 
2. [mySQL Workbench](https://www.mysql.com/products/workbench/)
    - must be downloaded to manage database connection


## Library
- mysql-connector-python

Remember to install the package with the following command
```
pip install <the name of the package>
```

## Important functions
- sql.connector.connect(host, user_name, user_password)
- sql.connector.cursor()
- sql.connector.cursor().execute(query)
- [sql.connector.commit()](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html)
    - to commit the current transaction, by default Python does not autocommit (commiting is one of the way for isolation level)

## Resources
- [freeCodeCamp](https://www.freecodecamp.org/news/connect-python-with-sql/)