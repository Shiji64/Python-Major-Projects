import random

from player import level_up
from game_data import enemies, skills, potions, bosses


def create_enemy(player):

    available_enemies = []

    for enemy in enemies:

        if enemy["min_level"] <= player["level"] <= enemy["max_level"]:
            available_enemies.append(enemy)

    enemy = random.choice(available_enemies).copy()

    # Scale enemy according to player level
    level_difference = player["level"] - enemy["min_level"]
    scale = 1 + (level_difference * 0.05)

    enemy["hp"] = int(enemy["hp"] * scale)
    enemy["attack"] = int(enemy["attack"] * scale)
    enemy["defense"] = int(enemy["defense"] * scale)

    enemy["max_hp"] = enemy["hp"]
    enemy["level"] = player["level"]

    return enemy

def use_skill(player, enemy):

    player_skills = skills[player["class"]]

    print("\n----- SKILLS -----")

    for i in range(len(player_skills)):
        skill = player_skills[i]

        print(
            f"{i + 1}. {skill['name']} "
            f"- Mana: {skill['mana']}"
        )
    print("5. Back")
    ch = input("Choose skill: ").strip()
    if ch == "5":
        return False
    try:
        skill_no = int(ch) - 1
        if skill_no < 0 or skill_no >= len(player_skills):
            print("Invalid skill!")
            return False
        selected_skill = player_skills[skill_no]
        if player["mana"] < selected_skill["mana"]:
            print("Not enough mana!")
            return False
        player["mana"] -= selected_skill["mana"]
        damage = int(
            player["attack"] * selected_skill["multiplier"]
            - enemy["defense"]
        )
        if damage < 1:
            damage = 1
        enemy["hp"] -= damage
        if enemy["hp"] < 0:
            enemy["hp"] = 0
        print(
            f"\nYou used {selected_skill['name']}!"
        )
        print(f"You dealt {damage} damage!")
        print(
            f"Mana remaining: "
            f"{player['mana']}/{player['max_mana']}"
        )
        return True

    except ValueError:
        print("Please enter a valid number!")
        return False


def use_potion(player):
    if len(player["potions"]) == 0:
        print("You have no potions!")
        return False
    print("\n----- POTIONS -----")
    for i in range(len(player["potions"])):
        print(f"{i + 1}. {player['potions'][i]}")
    print(f"{len(player['potions']) + 1}. Back")
    ch = input("Choose potion: ").strip()
    try:
        choice = int(ch)
        if choice == len(player["potions"]) + 1:
            return False
        if choice < 1 or choice > len(player["potions"]):
            print("Invalid potion!")
            return False
        potion_name = player["potions"][choice - 1]
        selected_potion = None
        for potion in potions:
            if potion["name"] == potion_name:
                selected_potion = potion
                break
        if selected_potion is None:
            print("Potion not found!")
            return False
        if selected_potion["type"] == "health":
            if player["hp"] == player["max_hp"]:
                print("Your HP is already full!")
                return False
            if selected_potion["amount"] == "full":
                player["hp"] = player["max_hp"]
            else:
                player["hp"] += selected_potion["amount"]
                if player["hp"] > player["max_hp"]:
                    player["hp"] = player["max_hp"]
            print(f"HP restored!")
            print(f"HP: {player['hp']}/{player['max_hp']}")
        elif selected_potion["type"] == "mana":
            if player["mana"] == player["max_mana"]:
                print("Your Mana is already full!")
                return False
            if selected_potion["amount"] == "full":
                player["mana"] = player["max_mana"]
            else:
                player["mana"] += selected_potion["amount"]
                if player["mana"] > player["max_mana"]:
                    player["mana"] = player["max_mana"]

            print("Mana restored!")
            print(f"Mana: {player['mana']}/{player['max_mana']}")
        elif selected_potion["type"] == "mixed":
            player["hp"] += selected_potion["hp"]
            player["mana"] += selected_potion["mana"]
            if player["hp"] > player["max_hp"]:
                player["hp"] = player["max_hp"]
            if player["mana"] > player["max_mana"]:
                player["mana"] = player["max_mana"]

            print("HP and Mana restored!")
            print(f"HP: {player['hp']}/{player['max_hp']}")
            print(f"Mana: {player['mana']}/{player['max_mana']}")
        player["potions"].pop(choice - 1)
        print(f"You used {selected_potion['name']}!")
        return True
    except ValueError:
        print("Please enter a valid number!")
        return False   

def create_boss(player):

    boss = bosses[player["level"]].copy()

    boss["level"] = player["level"]
    boss["max_hp"] = boss["hp"]
    boss["is_boss"] = True

    return boss

def battle(player, enemy):

    print(f"\nA {enemy['name']} appeared!")

    while player["hp"] > 0 and enemy["hp"] > 0:
        print("\n" + "-"*20)
        print(f"{player['name']} HP: {player['hp']}/{player['max_hp']}")
        print(f"{enemy['name']} HP: {enemy['hp']}/{enemy['max_hp']}")
        print("-"*20)
        ch = input("\nYour Turn \n1. Attack\n2. Skills\n3. Use Potion\n4. Defend\n5. View Stats\n6. Run\nEnter your choice: ").strip()
        defending = False
        if ch == "1":
            damage = player["attack"] - enemy["defense"]
            if damage < 1:
                damage = 1
            # Check critical hit
            if random.randint(1, 100) <= player["crit_chance"]:
                damage = int(damage * player["crit_damage"])
                print("CRITICAL HIT!")
            enemy["hp"] -= damage
            if enemy["hp"] < 0:
                enemy["hp"] = 0
            print(f"You dealt {damage} damage!")
        elif ch == "2":
            skill_used = use_skill(player, enemy)
            if not skill_used:
                continue
        elif ch == "3":
            potion_used = use_potion(player)
            if not potion_used:
                continue
        elif ch == "4":
            defending = True
            print("You are defending!")
        elif ch == "5":
            print("\n----- PLAYER STATS -----")
            print(f"Name: {player['name']}")
            print(f"Class: {player['class']}")
            print(f"Level: {player['level']}")
            print(f"HP: {player['hp']}/{player['max_hp']}")
            print(f"Mana: {player['mana']}/{player['max_mana']}")
            print(f"Attack: {player['attack']}")
            print(f"Defense: {player['defense']}")
            print(f"Gold: {player['gold']}")
            continue
        elif ch == "6":
            print("You escaped from the battle!")
            return
        else:
            print("Invalid option!")
            continue
        # Check if enemy is defeated
        if enemy["hp"] <= 0:
            print(f"\n{enemy['name']} defeated!")
            player["exp"] += enemy["exp"]
            player["gold"] += enemy["gold"]
            if enemy.get("is_boss", False):
                player["bosses_defeated"] += 1
                print("\n***** BOSS DEFEATED! *****")
                print(f"You defeated {enemy['name']}!")
                if enemy["name"] == "Ancient Demon King":
                    print("\n============================")
                    print("         VICTORY!")
                    print("============================")
                    print("The Ancient Demon King has been defeated!")
                    print("Peace has returned to Eldoria!")
                    if player["level"] == 100 and player["bosses_defeated"] >= 10:
                        return
            else:
                player["enemies_defeated"] += 1
            print(f"You gained {enemy['exp']} EXP")
            print(f"You gained {enemy['gold']} Gold")
            level_up(player)

            return

        # Enemy turn
        enemy_damage = enemy["attack"] - player["defense"]
        if enemy_damage < 1:
            enemy_damage = 1
        if defending:
            enemy_damage = enemy_damage // 2
            if enemy_damage < 1:
                enemy_damage = 1
        player["hp"] -= enemy_damage
        if player["hp"] < 0:
            player["hp"] = 0
        print(f"{enemy['name']} attacked you!")
        print(f"You received {enemy_damage} damage!")
    if player["hp"] <= 0:
        print("\n----- GAME OVER -----")
        return