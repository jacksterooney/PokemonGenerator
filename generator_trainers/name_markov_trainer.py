import sqlite3
import random

from db import database_connector


def build_markov_chain(name_list, n):
    chain = {
        '_initial': {},
        '_names': set(name_list)
    }
    for name in name_list:
        name_wrapped = str(name) + '.'
        for i in range(0, len(name_wrapped) - n):
            name_tuple = name_wrapped[i:i + n]
            name_next = name_wrapped[i + 1:i + n + 1]

            if name_tuple not in chain:
                entry = chain[name_tuple] = {}
            else:
                entry = chain[name_tuple]

            if i == 0:
                if name_tuple not in chain['_initial']:
                    chain['_initial'][name_tuple] = 1
                else:
                    chain['_initial'][name_tuple] += 1

            if name_next not in entry:
                entry[name_next] = 1
            else:
                entry[name_next] += 1
    return chain


def select_all_names():
    conn = database_connector.create_pokedb_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM pokemon")

        names = cur.fetchall()

        # De-hypenate names and Convert to regular list
        namelist = []
        for name in names:
            name_dehyphenated = name[0].split("-")[0]
            namelist.append(name_dehyphenated)

        return namelist


def select_random_item(items):
    rnd = random.random() * sum(items.values())
    for item in items:
        rnd -= items[item]
        if rnd < 0:
            return item


def generate(chain):
    name_tuple = select_random_item(chain['_initial'])
    result = [name_tuple]

    while True:
        name_tuple = select_random_item(chain[name_tuple])
        last_character = name_tuple[-1]
        if last_character == '.':
            break
        result.append(last_character)

    generated = ''.join(result)
    good_name_length = 3 < len(generated) < 12
    if generated not in chain['_names'] and len(generated) > 3 and good_name_length:
        return generated.capitalize()
    else:
        return generate(chain)


def generate_name():
    names = select_all_names()
    chain = build_markov_chain(names, 3)
    name = generate(chain)
    return name


if __name__ == "__main__":
    print(generate_name())
