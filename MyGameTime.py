# pip install requests
# pip install howlongtobeatpy

import requests
base_url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
from howlongtobeatpy import HowLongToBeat


# Returns the user's API key and 64bit ID
print("\n\nWelcome to the Game Time program! You'll need a registered Steam API Key\
as well as your 64bit Steam ID to begin.\n\n")

print("Hint: Can be found at steamcommunity.com/dev/apikey")
steam_api_key = input("Enter your steam API key: ") 

print("\nHint: Can be found underneath your username in the 'Account Details' menu")
bit_id = input("Enter you 64bit steam ID: ")


# Accesses the steam library data using creds from previous function
def get_steam_library(api_key, steam_id):
    url = f"{base_url}?key={api_key}&steamid={steam_id}&format=json&include_appinfo=1&include_played_free_games=1"
    response = requests.get(url)

    # If access attempt is successful, return the library data.
    # If attempt is unsuccessful, produce an error message
    if response.status_code == 200:
        # Converts response to JSON format
        steam_library = response.json()
        return steam_library
    else:
        print(f"Failed to retrieve data {response.status_code}")

# Sorts the data into variables so it is easier to work with
def define_steam_library ():
    user_data = get_steam_library(steam_api_key, bit_id)
    # Access the response key, then access the games key within
    # that key so we can sort the data
    games = user_data.get("response", {}).get("games", [])

    game_library = []
    for game in games:
        name = game.get("name", "Unknown")
        playtime_mins = game.get("playtime_forever", 0)
        appid = game.get("appid", 0)
        game_library.append({
            # Name of the game
            "name": name,
            # ID of the game, used to reference a game
            # In the API
            "appid": appid,
            # Minutes a game has been played
            "playtime_minutes": playtime_mins,
            # Converts minutes into hours
            "playtime_hours": round(playtime_mins / 60, 2)
        })
    return game_library

THELIST = define_steam_library()
import json
print("\n\n")
print(json.dumps(THELIST, indent=4))



#def cross_reference (steam_games):
#    for game in steam_games:
#        HowLongToBeat().search(game)
#        print()

#def main():
#    cross_reference(define_steam_library())
