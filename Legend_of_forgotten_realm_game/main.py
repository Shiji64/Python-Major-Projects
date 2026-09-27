from player import newgame, viewstats 
from battle import battle, create_enemy, create_boss 
from save_load import save_game, load_game



def instructions():
    print("\n----- INSTRUCTIONS -----")
    print("Choose a class and fight enemies.")
    print("Gain EXP and gold by defeating enemies.")
    print("Level up and defeat bosses every 10 levels.")
    print("Reach Level 100 and defeat the Ancient Demon King.")

def gamemenu(player):
    while True:
        if player["hp"] <= 0:
            print("Your character has been defeated!")
            return
        print("\n----- GAME MENU -----")
        print("1. Fight Enemy")
        print("2. View Stats")
        print("3. Inventory")
        print("4. Shop")
        print("5. Save Game")
        print("6. Exit to Main Menu")
        ch = input("Enter your choice: ").strip()
        if ch == "1":
            if (
                player["level"] % 10 == 0
                and player["bosses_defeated"] < player["level"] // 10
            ):
                print("\n***** BOSS BATTLE *****")
                enemy = create_boss(player)
            else:
                enemy = create_enemy(player)
            battle(player, enemy)
            if player["level"] == 100 and player["bosses_defeated"] >= 10:
                return
        elif ch == "2":
            viewstats(player)
        elif ch == "3":
            print("Inventory coming soon")
        elif ch == "4":
            print("Shop coming soon")
        elif ch == "5":
            save_game(player)
        elif ch == "6":
            return
        else:
            print("Invalid option!")

def main():
    while True:
        print("----- LEGENDS OF THE FORGOTTEN REALM -----")
        ch = input("1. New Game\n2. Continue\n3. Instructions\n4. Exit\nEnter your choice: ")
        if ch == "1":
            player = newgame()
            if player:
                gamemenu(player)
        elif ch == "2":
            player = load_game()

            if player:
                gamemenu(player)

        elif ch == "3":
            instructions()

        elif ch == "4":
            print("Thank you for playing!")
            break

        else:
            print("Invalid Option")

if __name__ == "__main__":
    main()