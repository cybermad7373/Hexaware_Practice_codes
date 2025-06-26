from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

load_dotenv()

try:
    engine = create_engine(
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )
    with engine.connect() as conn:
        print("DB Connected")

        # Create table
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255)
        )
        """))

        # Insert a row
        conn.execute(text("INSERT INTO users (name, email) VALUES (:name, :email)"),{"name": "ruthravarshan", "email": "rutrhaa@example.com"})

        # Select data
        result = conn.execute(text("SELECT * FROM users"))
        for row in result:
            print(row)

except SQLAlchemyError as e:
    print(" Error:", e)
