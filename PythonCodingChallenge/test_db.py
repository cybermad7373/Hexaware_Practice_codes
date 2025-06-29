from util.db_conn_util import DBConnUtil
from util.db_property_util import DBPropertyUtil

def test_connection():
    try:
        print("Testing database connection...")
        
        connection_string = DBPropertyUtil.get_connection_string("db.properties")
        print(f"Connection string: {connection_string}")
        
        # connection
        conn = DBConnUtil.get_connection(connection_string)
        
        if conn.is_connected():
            print("Connection successful!")
            print(f"MySQL server version: {conn.get_server_info()}")
            cursor = conn.cursor()
            cursor.execute("SELECT DATABASE()")
            db_name = cursor.fetchone()[0]
            print(f"Connected to database: {db_name}")
            
            cursor.close()
            conn.close()
            print("Connection closed.")
        else:
            print("Connection failed - no connection established")
            
    except Exception as e:
        print(f"Connection failed: {str(e)}")

if __name__ == "__main__":
    test_connection()