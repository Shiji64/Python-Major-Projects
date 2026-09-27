
def newgame():
    pname = input("Enter player name: -").strip()
    if pname == "":
        print("Player name cannot be empty!")
        return
    ch = input("\nChoose your class\n1. Warrior\n2. Mage\n3. Archer\n4. Assassin\nEnter your choice: ").strip()
    if ch == "1":
        pclass = "Warrior"
    elif ch == "2":
        pclass = "Mage"
    elif ch == "3":
        pclass = "Archer"
    elif ch == "4":
        pclass = "Assassin"
    else:
        print("Invalid class selection!")
        return

    print(f"\nPlayer Name : {pname}")
    print(f"Class : {pclass}")
    if pclass == "Warrior":
        max_hp = 150
        max_mana = 50
        attack = 25
        defense = 20
        crit_chance = 10

    elif pclass == "Mage":
        max_hp = 100
        max_mana = 150
        attack = 30
        defense = 10
        crit_chance = 15

    elif pclass == "Archer":
        max_hp = 110
        max_mana = 100
        attack = 22
        defense = 15
        crit_chance = 25

    elif pclass == "Assassin":
        max_hp = 90
        max_mana = 80
        attack = 28
        defense = 10
        crit_chance = 35
    player = {
        "name": pname,
        "class": pclass,
        "level": 1,
        "exp": 0,
        "hp": max_hp,
        "max_hp": max_hp,
        "mana": max_mana,
        "max_mana": max_mana,
        "attack": attack,
        "defense": defense,
        "gold": 100,
        "crit_chance": crit_chance,
        "crit_damage": 1.5,
        "weapon": None,
        "armor": None,
        "potions": [
            "Small Health Potion",
            "Small Health Potion",
            "Small Mana Potion"
        ],
        "inventory": [],
        "bosses_defeated": 0,
        "enemies_defeated": 0
    }
    print("\n----- PLAYER CREATED -----")
    print(f"Name : {player['name']}")
    print(f"Class : {player['class']}")
    print(f"HP : {player['hp']}/{player['max_hp']}")
    print(f"Mana : {player['mana']}/{player['max_mana']}")
    print(f"Attack : {player['attack']}")
    print(f"Defense : {player['defense']}")
    return player


def viewstats(player):
    print("\n----- PLAYER STATS -----")
    print(f"Name : {player['name']}")
    print(f"Class : {player['class']}")
    print(f"Level : {player['level']}")
    print(f"EXP : {player['exp']}")
    print(f"HP : {player['hp']}/{player['max_hp']}")
    print(f"Mana : {player['mana']}/{player['max_mana']}")
    print(f"Attack : {player['attack']}")
    print(f"Defense : {player['defense']}")
    print(f"Gold : {player['gold']}")
    print(f"Enemies Defeated : {player['enemies_defeated']}")
    print(f"Bosses Defeated : {player['bosses_defeated']}")


def level_up(player):
    exp_needed = player["level"] * 100
    while player["exp"] >= exp_needed and player["level"] < 100:
        # Boss gate
        if player["level"] % 10 == 0:
            required_bosses = player["level"] // 10
            if player["bosses_defeated"] < required_bosses:
                print(
                    f"\nYou must defeat the Level "
                    f"{player['level']} boss before progressing!"
                )
                break
        player["exp"] -= exp_needed
        player["level"] += 1
        player["max_hp"] += 10
        player["max_mana"] += 5
        player["attack"] += 3
        player["defense"] += 2
        # Restore HP and Mana after level up
        player["hp"] = player["max_hp"]
        player["mana"] = player["max_mana"]
        print("\n----- LEVEL UP! -----")
        print(f"You reached Level {player['level']}!")
        print(f"Max HP : {player['max_hp']}")
        print(f"Max Mana : {player['max_mana']}")
        print(f"Attack : {player['attack']}")
        print(f"Defense : {player['defense']}")

        exp_needed = player["level"] * 100