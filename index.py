# Task 1: Create database using SQLite
#Install & load sqlite3
#!pip install sqlite3  ##Uncomment the code to install sqlite3

import sqlite3

# Connecting to sqlite
# connection object
conn = sqlite3.connect('INSTRUCTOR2.db')

# cursor object
cursor_obj = conn.cursor()


# Task 2: Create a table in the database
# Before creating a table, let's first check if the table already exist or not. To drop the table from a database use DROP query. A cursor is an object which helps to execute the query and fetch the records from the database.
# Drop the table if it already exists.
# cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR2")

# Dont worry if you get this error:
# If you see an exception/error similar to the following, indicating that INSTRUCTOR is an undefined name, that's okay. It just implies that the INSTRUCTOR table does not exist in the table - which would be the case if you had not created it previously.

# Exception: [IBM][CLI Driver][DB2/LINUXX8664] SQL0204N "ABC12345.INSTRUCTOR" is an undefined name. SQLSTATE=42704 SQLCODE=-204

# Create table
# table = """ create table IF NOT EXISTS INSTRUCTOR2(
#     ID INTEGER PRIMARY KEY NOT NULL,
#     FNAME VARCHAR(20),
#     LNAME VARCHAR(20),
#     CITY VARCHAR(20),
#     CCODE CHAR(2)
# );"""

# cursor_obj.execute(table)
# print("Table is Ready")


# Task 3: Insert data into the table
# cursor_obj.execute("""INSERT INTO INSTRUCTOR2 VALUES (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')""")

# Now use a single query to insert the remaining two rows of data
# cursor_obj.execute('''insert into INSTRUCTOR2 values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')


# # Task 4: Query data in the table
statement = """SELECT * FROM INSTRUCTOR2"""
cursor_obj.execute(statement)

print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
    print(row_all)

# # Fetch few rows from the table
# # If you want to fetch few rows from the table we use fetchmany(bumberofrows) and mention the number of rows you want to fetch
output_many = cursor_obj.fetchmany(2)
for row_many in output_many:
    print(row_many)

# # Fetch only FNAME from the table
statement2 = """SELECT FNAME FROM INSTRUCTOR2"""
cursor_obj.execute(statement2)

print("All the data")
output_column = cursor_obj.fetchall()
for column_all in output_column:
    print(column_all)

# Bonus: now write and execute an update statement that changes the Rav's CITY to MOOSETOWN
query_update='''update INSTRUCTOR2 set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update)

statement = '''SELECT * FROM INSTRUCTOR2'''
cursor_obj.execute(statement)
  
print("All the data")
output1 = cursor_obj.fetchmany(2)
for row in output1:
  print(row)


# Task 5: Retrieve data into Pandas
import pandas as pd
#retrieve the query results into a pandas dataframe
df = pd.read_sql_query("select * from INSTRUCTOR2;", conn)

#print the dataframe
print(df)

#print just the LNAME for first row in the pandas data frame
print(df.LNAME[0])

df.shape


# Task 6: Close the Connection
# Close the connection
conn.close()