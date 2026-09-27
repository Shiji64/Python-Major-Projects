import json


def save_game(player):
    with open("savegame.json", "w") as file:
        json.dump(player, file, indent=4)

    print("Game saved successfully!")


def load_game():
    try:
        with open("savegame.json", "r") as file:
            player = json.load(file)

        print("Game loaded successfully!")
        return player

    except FileNotFoundError:
        print("No saved game found!")
        return None