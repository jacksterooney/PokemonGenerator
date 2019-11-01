import json
import markovify

from generator_trainers import name_markov_trainer, description_markov_trainer


def load_description_model():

    # Load data from json
    with open("generator_trainers/resources/description_markov_json.txt") as input_file:
        data = json.loads(input_file.read())
        model = markovify.Text.from_json(data)

    return model


# Stores for model data
name_markov_model = None
description_markov_model = load_description_model()


def generate_pokemon():
    name = name_markov_trainer.generate_name()
    description = description_markov_trainer.generate_description(name, description_markov_model)
    print(name)
    print(description)


if __name__ == '__main__':
    generate_pokemon()
