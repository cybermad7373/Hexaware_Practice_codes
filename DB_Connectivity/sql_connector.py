import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    if conn.is_connected():
        print("DB Connected")
        cursor = conn.cursor()

        #Create a table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255)
        )
        """)

        #Insert a row
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Rutrha", "ruthra@example.com"))
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("varshan", "varshan@example.com"))
        conn.commit()  # Commit changes in table

        #Select data
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            print(row)

        cursor.close()
        conn.close()

except Error as e:
    print(" Error:", e)
