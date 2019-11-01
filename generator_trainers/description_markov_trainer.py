import markovify
import json

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
            description = description.replace(name, "<POKEMON>").replace(str(name).capitalize(), "<POKEMON>")

            description_string += description + " "

        return description_string


def generate_and_save_description():
    words = select_all_descriptions()
    description_model = markovify.Text(words)
    model_json = description_model.to_json()

    with open("resources/description_markov_json.txt", 'w') as output_file:
        json.dump(model_json, output_file)


def generate_description(name, model):
    min_description_length = 100
    max_sentence_length = 250

    sentence = ""
    while len(sentence) < min_description_length:
        new_sentence = model.make_sentence()
        if len(sentence + new_sentence) > max_sentence_length:
            continue
        else:
            sentence += new_sentence + " "

    sentence = sentence.replace("<POKEMON>", str(name))
    return sentence


def load_description_model():

    # Load data from json
    with open("resources/description_markov_json.txt") as input_file:
        data = json.loads(input_file.read())
        model = markovify.Text.from_json(data)

    return model


if __name__ == "__main__":
    description = generate_description(name_markov_trainer.generate_name(), load_description_model())
    print(description)
