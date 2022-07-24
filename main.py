import requests
import json

pokemon_id = 3

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
pokemon_data = response.json()

# # Make the response look nice when we print it out
# pretty_pokemon_data = json.dumps(pokemon_data, indent=2)
# print(pretty_pokemon_data)

print(f"Name: {pokemon_data['name']}")
print(f"Weight: {pokemon_data['weight']}")
print(f"Height: {pokemon_data['height']}")
print(f"Base experience: {pokemon_data['base_experience']}")

for type_data in pokemon_data['types']:
    print(f"Type: {type_data['type']['name']}")

for move_data in pokemon_data['moves']:
    print(f"Move: {move_data['move']['name']}")

for ability_data in pokemon_data['abilities']:
    print(f"Ability: {ability_data['ability']['name']}")