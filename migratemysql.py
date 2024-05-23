import mysql.connector

# Connect to the source MySQL database
source_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Maryamtalha2102",
    database="userdatabase"
)
source_cursor = source_conn.cursor()

# Connect to the target MySQL database
target_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Maryamtalha2102",
    database="userdatabase_v2"
)
target_cursor = target_conn.cursor()

# Query data from source database
source_cursor.execute("SELECT UserID, Name, Email FROM Users")
rows = source_cursor.fetchall()

# Insert data into target database
insert_query = "INSERT INTO Users (UserID, Name, Email) VALUES (%s, %s, %s)"
for row in rows:
    target_cursor.execute(insert_query, row)

# Commit changes and close connections
target_conn.commit()
source_cursor.close()
source_conn.close()
target_cursor.close()
target_conn.close()

print("Data migration completed successfully.")
