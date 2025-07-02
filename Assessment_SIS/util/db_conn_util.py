import mysql.connector
from mysql.connector import Error
from mysql.connector.pooling import MySQLConnectionPool
from typing import Optional
from .db_property_util import get_connection_string

class DBConnUtil:
    """
    Utility class for managing MySQL database connections using connection pooling
    """
    _pool: Optional[MySQLConnectionPool] = None
    
    @classmethod
    def get_connection(cls):
        """
        Get a database connection from the connection pool
        
        Returns:
            MySQLConnection: A connection from the pool
            
        Raises:
            Exception: If connection pool creation or connection fails
        """
        if cls._pool is None:
            try:
                db_config = get_connection_string()
                cls._pool = MySQLConnectionPool(
                    pool_name="sis_pool",
                    pool_size=5,
                    pool_reset_session=True,
                    **db_config
                )
            except Error as e:
                raise Exception(f"Error creating connection pool: {e}")
        
        try:
            connection = cls._pool.get_connection()
            connection.autocommit = False  # We'll manage transactions manually
            return connection
        except Error as e:
            raise Exception(f"Error getting connection from pool: {e}")
    
    @classmethod
    def close_pool(cls):
        """Close all connections in the pool"""
        if cls._pool:
            cls._pool.close()
            cls._pool = None