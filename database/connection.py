import mysql.connector
from config.config import DB_CONFIG


def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            print("✅ Database Connected Successfully")

        return connection

    except mysql.connector.Error as err:
        print(f"❌ Error : {err}")
        return None