import json
import markovify

from generator_trainers import name_markov_trainer, description_markov_trainer

# Stores for model data
name_markov_model = None
description_markov_model = description_markov_trainer.load_description_model()


def generate_pokemon():
    name = name_markov_trainer.generate_name()
    description = description_markov_trainer.generate_description(name, description_markov_model)
    print(name)
    print(description)


if __name__ == '__main__':
    generate_pokemon()
