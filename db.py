import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def connection():
    try:

        conn = mysql.connector.connect(
            host = os.getenv("host"),
            user = os.getenv("user"),
            password = os.getenv("password"),
            database = os.getenv("database")
        )
        return conn
    except Exception as e :
        print("Erreur de connexion à la base de données :", e)
        return None