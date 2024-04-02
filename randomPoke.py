import requests
import random

def get_pokemon_by_id(pokemon_id):
    # Construct the URL for the API call
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    
    # Make the GET request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        pokemon_data = response.json()
        
        # Extract and print the name and ID of the Pokemon
        print(f"ID: {pokemon_data['id']}, Name: {pokemon_data['name']}")
    else:
        print(f"Failed to retrieve Pokemon data. Status code: {response.status_code}")

def main():
    # Generate a random number between 1 and 898
    random_id = random.randint(1, 898)
    
    # Call the function to get and print the Pokemon data
    get_pokemon_by_id(random_id)

if __name__ == "__main__":
    main()