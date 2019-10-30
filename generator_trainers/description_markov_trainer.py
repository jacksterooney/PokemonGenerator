import markovify

from db import database_connector
from generator_trainers import name_markov_trainer


def select_all_descriptions():
    conn = database_connector.create_pokedb_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT name, description FROM pokemon")

        names_and_descriptions = cur.fetchall()

        # Convert all descriptions into one long regular list
        description_string = ""
        for names_and_description in names_and_descriptions:
            name = names_and_description[0]
            description = str(names_and_description[1])

            # Replace instances of the pokemon name with a keyword
            description = description.replace('♂', '')
            description = description.replace('♀', '')
            description = description.replace(str(name).capitalize(), "<POKEMON>")

            description_string += description + " "

        return description_string


def generate_description(name):
    words = select_all_descriptions()
    description_model = markovify.Text(words)

    min_description_length = 64
    max_sentence_length = 226

    sentence = ""
    while len(sentence) < min_description_length:
        new_sentence = description_model.make_sentence()
        if len(sentence + new_sentence) > max_sentence_length:
            continue
        else:
            sentence += new_sentence + " "

    sentence = sentence.replace("<POKEMON>", str(name))

    print(name)
    print(sentence)


if __name__ == "__main__":
    generate_description(name_markov_trainer.generate_name())
