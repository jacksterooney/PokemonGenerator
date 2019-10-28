import pokebase as pb


def get_pokemon(pokemon_id):
    pokemon = pb.NamedAPIResource('pokemon', pokemon_id)

    # Get types as array
    types = []
    for pokemon_type in pokemon.types:
        types.append(pokemon_type.type.name)

    # Get flavor text
    pokemon_species = pb.NamedAPIResource('pokemon-species', pokemon_id)
    flavor_text_entries = pokemon_species.flavor_text_entries

    flavor_text = None
    for entry in flavor_text_entries:
        if entry.language.name == 'en':
            flavor_text = entry.flavor_text
            break

    if flavor_text is None:
        raise Exception("Could not find flavor text!")

    # Return list of stats
    return pokemon.name, str(types), pokemon.height, pokemon.weight, flavor_text


def get_pokemon_sprite(pokemon_id):
    sprite = pb.NamedAPIResource('pokemon', pokemon_id).sprites.front_default
    return sprite


if __name__ == '__main__':
    print(get_pokemon(1))
    print(get_pokemon_sprite(1))
