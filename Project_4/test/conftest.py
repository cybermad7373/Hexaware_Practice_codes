import pytest
from database.db_connection import create_connection

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Setup test database before tests run"""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Clear test data
            cursor.execute("DELETE FROM bill_shares")
            cursor.execute("DELETE FROM bills")
            cursor.execute("DELETE FROM questions")
            cursor.execute("DELETE FROM quizzes")
            cursor.execute("DELETE FROM marks")
            cursor.execute("DELETE FROM students")
            cursor.execute("DELETE FROM expenses")
            conn.commit()
        finally:
            conn.close()