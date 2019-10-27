from sqlite3 import Error

from db import database_connector


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    sql_create_pokemon_table = """ CREATE TABLE IF NOT EXISTS pokemon (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        type text NOT NULL,
                                        height integer NOT NULL,
                                        description text NOT NULL
                                    ); """

    sql_create_sprites_table = """ CREATE TABLE IF NOT EXISTS pokemon_sprites (
                               id integer PRIMARY KEY,
                               pokemon_id integer NOT NULL,
                               sprite blob NOT NULL,
                               FOREIGN KEY (pokemon_id) REFERENCES pokemon (id)
                               ); """

    # create a database connection
    conn = database_connector.create_pokedb_connection()

    # create tables
    if conn is not None:
        # create pokemon table
        create_table(conn, sql_create_pokemon_table)

        # create sprites table
        create_table(conn, sql_create_sprites_table)
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    main()
