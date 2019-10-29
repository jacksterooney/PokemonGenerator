import os
import sqlite3
from sqlite3 import Error


def create_pokedb_connection():
    database = os.path.dirname(os.path.realpath(__file__)) + r"\pokedb.db"
    print("Creating connection to " + database)
    return create_connection(database)


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
