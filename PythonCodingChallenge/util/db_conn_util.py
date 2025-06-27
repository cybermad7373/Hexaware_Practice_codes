import mysql.connector
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection(connection_string=None):
        try:
            if connection_string is None:
                # Get connection string from property file
                connection_string = DBPropertyUtil.get_connection_string("db.properties")
            
            # Parse the connection string
            params = {}
            for item in connection_string.split():
                key, value = item.split('=')
                params[key] = value
            
            # Establish connection
            connection = mysql.connector.connect(
                host=params.get('host'),
                database=params.get('dbname'),
                user=params.get('user'),
                password=params.get('password')
            )
            
            print("Connection established successfully")
            return connection
        except Exception as e:
            print(f"Error establishing database connection: {e}")
            raise