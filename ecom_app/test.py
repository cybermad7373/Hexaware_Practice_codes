from util.db_conn_util import DBConnUtil

conn = DBConnUtil.get_connection()
if conn:
    print("Connected successfully!")
    conn.close()
else:
    print("Connection failed.")
