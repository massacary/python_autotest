import requests


response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
                        json={
                            "name": "пыкачу",
                            "photo": "https://dolnikov.ru/pokemons/albums/006.png"
                             },
                        headers={'Trainer_token': 'adeb330a54430a8c8567cccf006caf68', 'Content-Type': 'application/json'}, timeout=5)

print(f'Code: {response.status_code} - {response.reason}. Message {response.text} ')

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
                        json={
                            "pokemon_id": "21273",
                            "name": "Драко",
                            "photo": "https://dolnikov.ru/pokemons/albums/007.png"
                             },
                        headers={'Trainer_token': 'adeb330a54430a8c8567cccf006caf68', 'Content-Type': 'application/json'}, timeout=5)

print(f'Code: {response.status_code} - {response.reason}. Message {response.text} ')

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                        json={
                            "pokemon_id": "21273",
                             },
                        headers={'Trainer_token': 'adeb330a54430a8c8567cccf006caf68', 'Content-Type': 'application/json'}, timeout=5)

print(f'Code: {response.status_code} - {response.reason}. Message {response.text} ')