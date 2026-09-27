# Legends of the Forgotten Realm

A command-line turn-based RPG developed in Python.

## Project Overview

The player creates a character, chooses a class, fights enemies, gains EXP and gold, levels up, uses class skills and potions, fights bosses at milestone levels, and can save or continue the game using JSON.

This project was developed as a Python major project to demonstrate functions, loops, conditional statements, lists, dictionaries, file handling, exception handling, the `random` module, the `json` module, and modular programming using multiple Python files.

## Features Implemented

- Character creation with player name
- Four character classes:
  - Warrior
  - Mage
  - Archer
  - Assassin
- Different HP, Mana, Attack, Defense, and Critical Chance for each class
- Turn-based battle system
- Normal attacks
- Critical hits
- Defend option
- Class-specific skills using Mana
- Health, Mana, and Mixed potion use
- Random enemy selection based on player level
- Enemy stat scaling
- EXP and Gold rewards
- Level-up system
- HP, Mana, Attack, and Defense increases on level-up
- Boss battles every 10 levels
- Boss progression up to the Ancient Demon King
- Game Over and Victory messages
- Save game using JSON
- Continue game by loading JSON save data
- Modular code using multiple `.py` files

## Project Files

```text
Legends_of_the_Forgotten_Realm/
|
|-- main.py
|-- player.py
|-- battle.py
|-- game_data.py
|-- save_load.py
|-- savegame.json
|-- README.md
```

### File Purpose

**main.py**  
Contains the main menu, instructions, game menu, and controls the overall game flow.

**player.py**  
Contains character creation, player statistics, and the level-up system.

**battle.py**  
Contains enemy creation, boss creation, battle logic, skills, potion use, critical hits, and defend mechanics.

**game_data.py**  
Stores game data such as enemies, skills, potions, bosses, and available weapon records.

**save_load.py**  
Contains the JSON save and load functions.

**savegame.json**  
Stores the saved player state when the player selects Save Game.

## Requirements

- Python 3.x
- No external Python libraries are required.

The project uses only Python standard-library modules such as:

```python
import random
import json
```

## How to Run

1. Keep all project files in the same folder.
2. Open a terminal or command prompt in that folder.
3. Run:

```bash
python main.py
```

4. The main menu will appear:

```text
----- LEGENDS OF THE FORGOTTEN REALM -----
1. New Game
2. Continue
3. Instructions
4. Exit
```

## How to Play

### New Game

Select **New Game**, enter the player name, and choose one of the four classes.

Each class has different starting statistics.

### Game Menu

After creating a character, the game menu provides options to fight enemies, view player stats, save the game, and return to the main menu.

### Battle

During battle, the player can:

```text
1. Attack
2. Skills
3. Use Potion
4. Defend
5. View Stats
6. Run
```

After the player's action, the enemy gets a turn if it is still alive.

### Skills

Each class has four different skills. Skills consume Mana and can deal more damage than a normal attack.

### Potions

The implemented potion system supports Health, Mana, and Mixed potions. Potions are removed from the player's potion list after successful use.

### Leveling

The player gains EXP and Gold after defeating enemies. When enough EXP is collected, the player levels up and receives increases to:

- Maximum HP
- Maximum Mana
- Attack
- Defense

### Boss Battles

A boss battle occurs at every 10th level.

Boss progression:

```text
Level 10  - Goblin King
Level 20  - Forest Guardian
Level 30  - Ancient Golem
Level 40  - Vampire Lord
Level 50  - Dragon Rider
Level 60  - Demon General
Level 70  - Ice Titan
Level 80  - Shadow Emperor
Level 90  - Celestial Dragon
Level 100 - Ancient Demon King
```

The player must defeat the required boss before progressing beyond the level milestone.

### Save and Continue

Select **Save Game** from the game menu to save the current player data to `savegame.json`.

Select **Continue** from the main menu to load the previously saved game.

If no save file exists, the program displays a message instead of crashing.

## Current Project Scope

The current version focuses on the main playable systems: character creation, combat, class skills, potions, enemies, leveling, bosses, and JSON save/load.

Some assignment features are not fully implemented in this version. The Inventory and Shop menu options are placeholders, and the complete weapon/armor equipment, loot-drop, and world-region systems are not finished.

## Input Validation and Error Handling

The project includes validation for invalid menu choices, invalid skill and potion selections, insufficient Mana, empty player names, and missing save files.

`try/except` is used where numeric input is required and when loading a save file that may not exist.

## Notes

- Start a normal submission version of the game at Level 1.
- `savegame.json` can contain a sample saved game.
- All `.py` files must remain in the same folder so the imports work correctly.

## Author

Python Major Project  
Legends of the Forgotten Realm
