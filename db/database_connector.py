import sqlite3
from sqlite3 import Error
import os


def create_pokedb_connection():
    return create_connection(os.getcwd() + r"\pokedb.db")


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
