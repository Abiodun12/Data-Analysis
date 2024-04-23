import requests

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    weight = data['weight']
    types = [poke_type['type']['name'] for poke_type in data['types']]
    return {'abilities': abilities, 'weight': weight, 'types': types}

def create_pokemon(name):
    pokemon_data = get_pokemon_data(name)
    return {name: pokemon_data}

def create_pokemon_list(pokemon_names):
    pokemon_dict = {}
    for name in pokemon_names:
        pokemon_dict.update(create_pokemon(name))
    return pokemon_dict

def categorize_pokemon(pokemon_dict):
    categorized_pokemon = {}
    for name, data in pokemon_dict.items():
        for poke_type in data['types']:
            if poke_type not in categorized_pokemon:
                categorized_pokemon[poke_type] = {}
            categorized_pokemon[poke_type][name] = data
    return categorized_pokemon

def main():
    pokemon_names = ['charizard', 'ninetales', 'blastoise', 'lapras', 'pikachu',
                     'alakazam', 'gengar', 'dragonite', 'snorlax', 'gyarados',
                     'arcanine', 'machamp', 'venusaur', 'jolteon', 'golem',
                     'onix', 'vaporeon', 'scyther', 'magmar', 'articuno']
    pokemon_dict = create_pokemon_list(pokemon_names)
    categorized_pokemon = categorize_pokemon(pokemon_dict)
    for poke_type, pokemon in categorized_pokemon.items():
        print(f"{poke_type}:")
        for name, data in pokemon.items():
            print(f"\t{name}:")
            print(f"\t\tAbilities: {data['abilities']}")
            print(f"\t\tWeight: {data['weight']}")
            print("\t\t---")
        print()

if __name__ == "__main__":
    main()
