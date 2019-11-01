import pokebase as pb


def get_pokemon(pokemon_id):
    pokemon = pb.NamedAPIResource('pokemon', pokemon_id)

    # Get types as array
    types = []
    for pokemon_type in pokemon.types:
        types.append(pokemon_type.type.name)

    # Get flavor text
    flavor_text = get_flavor_text(pokemon_id, pokemon.name)

    if flavor_text is None:
        raise Exception("Could not find flavor text!")

    # Return list of stats
    return pokemon.name, str(types), pokemon.height, pokemon.weight, flavor_text


def get_flavor_text(pokemon_id, name):
    pokemon_species = pb.NamedAPIResource('pokemon-species', pokemon_id)
    flavor_text_entries = pokemon_species.flavor_text_entries
    english_flavor_text_entries = []
    flavor_text = ""

    # Get english entries
    for entry in flavor_text_entries:
        # Filter for english text
        if entry.language.name == 'en':
            # Remove line breaks, replace with space. Filter through duplicates where the pokemon name changes.
            filtered_flavor_text = str(entry.flavor_text).replace('\n', ' ').replace('\r', '').replace("\x0c", " ")
            filtered_flavor_text = filtered_flavor_text.replace(name, str(name).lower())\
                .replace(str(name).upper(), str(name).lower()).replace(str(name).capitalize(), str(name).lower())

            english_flavor_text_entries.append(filtered_flavor_text)

    # Delete repeated entries
    english_flavor_text_entries = list(dict.fromkeys(english_flavor_text_entries))
    for entry in english_flavor_text_entries:
        flavor_text += entry + " "

    return flavor_text


def get_pokemon_sprite(pokemon_id):
    sprite = pb.NamedAPIResource('pokemon', pokemon_id).sprites.front_default
    return sprite


if __name__ == '__main__':
    print(get_pokemon(1))
    print(get_pokemon_sprite(1))
