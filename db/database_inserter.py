from db import database_connector, pokeapi_collector


def insert_pokemon(conn, pokemon):
    """Create a new pokemon in the pokemon table
    :param conn:
    :param pokemon:
    :return pokemon id
    """
    sql = '''INSERT INTO pokemon(name, type, height, weight, description)
             VALUES (?,?,?,?,?)'''

    cur = conn.cursor()
    cur.execute(sql, pokemon)
    return cur.lastrowid


def populate_pokemon():
    conn = database_connector.create_pokedb_connection()
    with conn:
        # Loop over all pokemon ids
        for i in range(1, 808):
            pokemon = pokeapi_collector.get_pokemon(i)
            percent_complete = str(float("{0:.2f}".format((i/808) * 100)))
            print("Inserting " + pokemon[0] + " - " + percent_complete + "% complete")
            insert_pokemon(conn, pokemon)


if __name__ == '__main__':
    populate_pokemon()
