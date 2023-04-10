import requests as r
import shutil
import ascii_magic as magic

# check out this Pokemon API https://pokeapi.co/ 
# Use the requests package to connect to this API and 
# get and store data for 5 different pokemon. 
# Get the pokemons: name, atleast one ability's name, base_experience, and the URL for its sprite (an image that shows up on screen) for the 'front_shiny', 
# attack base_stat, hp base_stat, defense base_stat

# pokemon = r.get("https://pokeapi.co/api/v2/pokemon/1/")
# data = pokemon.json()
# print(f"{data['name'].title()}\n")  #pokemon name
# print(f"Abilities:\n{data['abilities'][0]['ability']['name'].title()}") #pokemon ability
# print(f"{data['abilities'][1]['ability']['name'].title()}")
# print(f"\nBase experience: {data['base_experience']}") #base experience

# imageurl = data['sprites']['front_shiny']
# image = r.get(imageurl, stream = True)
# with open(data['name'], 'wb') as f:
#     shutil.copyfileobj(image.raw, f)

# poke_art = magic.from_image(data['name'])
# poke_art.to_terminal(
#     columns = 100,
#     width_ratio = 2.2
# )



def pokeDex():
        cont = True
        while cont == True:
            str = input("What Pokemon would you like to look up? You can enter a number or a name of a valid pokemon: ")
            try:
                 pokemon = r.get(f"https://pokeapi.co/api/v2/pokemon/{int(str)}/")
            except:
                pokemon = r.get(f"https://pokeapi.co/api/v2/pokemon/{str.lower()}/")
            if pokemon.ok:
                data = pokemon.json()
                print(f"\n{data['name'].title()}")  #pokemon name
                print(f"Pokemon #{data['id']}\n")
                print(f"Abilities")
                print(f"- {data['abilities'][0]['ability']['name'].title()}") #pokemon ability
                print(f"- {data['abilities'][1]['ability']['name'].title()}")
                print(f"\nBase experience: {data['base_experience']}") #base experience
                print("\nStats")
                print(f"- ATK: {data['stats'][1]['base_stat']}")
                print(f"- DEF: {data['stats'][2]['base_stat']}")
                print(f"- HP: {data['stats'][0]['base_stat']}")

                imageurl = data['sprites']['front_shiny'] #gets image url
                image = r.get(imageurl, stream = True)  #makes a request for the sppecific image
                with open(data['name'], 'wb') as f: 
                    shutil.copyfileobj(image.raw, f)    #saves image as a binary file with pokemon name as file name

                poke_art = magic.from_image(data['name'])   #creates and prints image to terminal
                poke_art.to_terminal(
                    columns = 100,
                    width_ratio = 2.2
                )

                more = input("Would you like to look up another pokemon? (y/n) or press Enter: ")
                if more.lower() == 'n':
                     cont = False
                if more.lower() == 'y':
                     cont == True
            else:
                print("I'm sorry that's not a valid entry...")

pokeDex()