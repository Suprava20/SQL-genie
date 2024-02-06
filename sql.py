import mysql.connector

# Establish a connection to the database
connection = mysql.connector.connect(
    host="localhost",  # Replace with your database host
    user="root",  # Replace with your database username
    password="kiit",  # Replace with your database password
    database="project"  # Replace with your database name
)

# Create a cursor
cursor = connection.cursor()

# Define the table creation SQL
table_info = """
CREATE TABLE student (
    Name VARCHAR(25),
    class VARCHAR(25),
    section VARCHAR(25),
    marks INT
);
"""

# Execute the table creation SQL
cursor.execute(table_info)

# Insert data into the table
cursor.execute('''INSERT INTO student VALUES ('Krish', 'data science', 'A', 90)''')
cursor.execute('''INSERT INTO student VALUES ('Sudhansu', 'data science', 'B', 100)''')
cursor.execute('''INSERT INTO student VALUES ('Daris', 'data science', 'A', 86)''')
cursor.execute('''INSERT INTO student VALUES ('Viskash', 'DevOPs', 'A', 50)''')
cursor.execute('''INSERT INTO student VALUES ('Dipesh', 'DevOPs', 'A', 35)''')

# Commit the changes
connection.commit()

# Print the inserted records
cursor.execute('''SELECT * FROM student''')
data = cursor.fetchall()

print("The inserted records are:")
for row in data:
    print(row)

# Close the connection
connection.close()
