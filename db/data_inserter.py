import pokebase as pb


def get_pokemon_stats(pokemon_id):
    pokemon = pb.NamedAPIResource('pokemon', pokemon_id)
    return pokemon_id, pokemon.name, pokemon.type, pokemon.height, pokemon.weight


def get_pokemon_flavor_text(pokemon_id):
    pokemon_species = pb.NamedAPIResource('pokemon-species', pokemon_id)
    flavor_text_entries = pokemon_species.flavor_text_entries

    for entry in flavor_text_entries:
        if entry.language.name == 'en':
            return entry.flavor_text

    print("Could not find any flavor text!")


def get_pokemon_sprite(pokemon_id):
    sprite = pb.NamedAPIResource('pokemon', pokemon_id).sprites.front_default
    return sprite


if __name__ == '__main__':
    print(get_pokemon_stats(32))
    print(get_pokemon_flavor_text(32))
    print(get_pokemon_sprite(32))
