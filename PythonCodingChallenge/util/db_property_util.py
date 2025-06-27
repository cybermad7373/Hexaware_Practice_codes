import configparser
import os

class DBPropertyUtil:
    @staticmethod
    def get_connection_string(property_file_name):
        try:
            config = configparser.ConfigParser()
            
            # Get the absolute path to the property file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            property_file_path = os.path.join(current_dir, "..", "database", property_file_name)
            
            print(f"Looking for property file at: {property_file_path}")  # Debug print
            
            if not os.path.exists(property_file_path):
                raise FileNotFoundError(f"Property file not found at: {property_file_path}")
            
            config.read(property_file_path)
            
            if 'mysql' in config:
                host = config['mysql']['host']
                database = config['mysql']['database']
                user = config['mysql']['user']
                password = config['mysql']['password']
                
                return f"host={host} dbname={database} user={user} password={password}"
            else:
                raise Exception("MySQL configuration not found in property file")
        except Exception as e:
            print(f"Error reading property file: {e}")
            raise