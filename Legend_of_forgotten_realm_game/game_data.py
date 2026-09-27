
weapons = [
    {
        "name": "Wooden Sword",
        "rank": "Common",
        "damage": 5,
        "crit_bonus": 0,
        "price": 50,
        "required_level": 1
    },

    {
        "name": "Iron Sword",
        "rank": "Rare",
        "damage": 15,
        "crit_bonus": 5,
        "price": 200,
        "required_level": 5
    }
]

enemies = [

    # Level 1 - 10
    {"name": "Goblin", "min_level": 1, "max_level": 10,
     "hp": 60, "attack": 15, "defense": 5, "exp": 50, "gold": 25},

    {"name": "Wolf", "min_level": 1, "max_level": 10,
     "hp": 55, "attack": 17, "defense": 4, "exp": 55, "gold": 20},

    {"name": "Slime", "min_level": 1, "max_level": 10,
     "hp": 70, "attack": 12, "defense": 6, "exp": 45, "gold": 20},

    {"name": "Zombie", "min_level": 1, "max_level": 10,
     "hp": 80, "attack": 14, "defense": 7, "exp": 60, "gold": 25},

    {"name": "Skeleton", "min_level": 1, "max_level": 10,
     "hp": 65, "attack": 18, "defense": 5, "exp": 65, "gold": 30},

    # Level 11 - 20
    {"name": "Orc", "min_level": 11, "max_level": 20,
     "hp": 120, "attack": 25, "defense": 12, "exp": 100, "gold": 45},

    {"name": "Bandit", "min_level": 11, "max_level": 20,
     "hp": 100, "attack": 28, "defense": 10, "exp": 105, "gold": 55},

    {"name": "Troll", "min_level": 11, "max_level": 20,
     "hp": 150, "attack": 24, "defense": 15, "exp": 120, "gold": 50},

    {"name": "Dark Archer", "min_level": 11, "max_level": 20,
     "hp": 90, "attack": 30, "defense": 9, "exp": 110, "gold": 60},

    {"name": "Giant Spider", "min_level": 11, "max_level": 20,
     "hp": 110, "attack": 27, "defense": 11, "exp": 115, "gold": 50},

    # Level 21 - 30
    {"name": "Vampire", "min_level": 21, "max_level": 30,
     "hp": 180, "attack": 38, "defense": 18, "exp": 160, "gold": 75},

    {"name": "Werewolf", "min_level": 21, "max_level": 30,
     "hp": 200, "attack": 40, "defense": 17, "exp": 170, "gold": 80},

    {"name": "Necromancer", "min_level": 21, "max_level": 30,
     "hp": 160, "attack": 45, "defense": 14, "exp": 180, "gold": 90},

    {"name": "Ice Golem", "min_level": 21, "max_level": 30,
     "hp": 240, "attack": 34, "defense": 25, "exp": 190, "gold": 85},

    {"name": "Fire Demon", "min_level": 21, "max_level": 30,
     "hp": 190, "attack": 48, "defense": 18, "exp": 200, "gold": 100},

    # Level 31 - 50
    {"name": "Desert Scorpion", "min_level": 31, "max_level": 50,
     "hp": 260, "attack": 55, "defense": 25, "exp": 250, "gold": 120},

    {"name": "Sand Warrior", "min_level": 31, "max_level": 50,
     "hp": 280, "attack": 58, "defense": 28, "exp": 270, "gold": 130},

    {"name": "Ancient Knight", "min_level": 31, "max_level": 50,
     "hp": 300, "attack": 60, "defense": 32, "exp": 290, "gold": 140},

    {"name": "Dark Wizard", "min_level": 31, "max_level": 50,
     "hp": 240, "attack": 70, "defense": 22, "exp": 310, "gold": 150},

    {"name": "Stone Guardian", "min_level": 31, "max_level": 50,
     "hp": 350, "attack": 55, "defense": 38, "exp": 320, "gold": 150},

    # Level 51 - 100
    {"name": "Lava Beast", "min_level": 51, "max_level": 100,
     "hp": 450, "attack": 85, "defense": 40, "exp": 450, "gold": 200},

    {"name": "Frost Giant", "min_level": 51, "max_level": 100,
     "hp": 500, "attack": 80, "defense": 45, "exp": 470, "gold": 220},

    {"name": "Sky Warrior", "min_level": 51, "max_level": 100,
     "hp": 420, "attack": 95, "defense": 38, "exp": 490, "gold": 230},

    {"name": "Shadow Demon", "min_level": 51, "max_level": 100,
     "hp": 440, "attack": 100, "defense": 40, "exp": 520, "gold": 250},

    {"name": "Demon Knight", "min_level": 51, "max_level": 100,
     "hp": 550, "attack": 95, "defense": 50, "exp": 550, "gold": 275}
]

skills = {

    "Warrior": [
        {"name": "Slash", "mana": 10, "multiplier": 1.2},
        {"name": "Shield Bash", "mana": 15, "multiplier": 1.4},
        {"name": "Rage", "mana": 25, "multiplier": 1.7},
        {"name": "Earthquake", "mana": 40, "multiplier": 2.2}
    ],

    "Mage": [
        {"name": "Fireball", "mana": 15, "multiplier": 1.4},
        {"name": "Ice Blast", "mana": 20, "multiplier": 1.6},
        {"name": "Thunder Strike", "mana": 30, "multiplier": 2.0},
        {"name": "Meteor", "mana": 50, "multiplier": 2.6}
    ],

    "Archer": [
        {"name": "Multi Shot", "mana": 10, "multiplier": 1.3},
        {"name": "Poison Arrow", "mana": 18, "multiplier": 1.5},
        {"name": "Explosive Arrow", "mana": 28, "multiplier": 1.9},
        {"name": "Sniper Shot", "mana": 40, "multiplier": 2.4}
    ],

    "Assassin": [
        {"name": "Backstab", "mana": 12, "multiplier": 1.5},
        {"name": "Smoke Strike", "mana": 18, "multiplier": 1.6},
        {"name": "Shadow Strike", "mana": 30, "multiplier": 2.1},
        {"name": "Instant Kill", "mana": 50, "multiplier": 3.0}
    ]
}

potions = [

    # Health Potions
    {"name": "Small Health Potion", "type": "health", "amount": 50, "price": 25},
    {"name": "Medium Health Potion", "type": "health", "amount": 100, "price": 50},
    {"name": "Large Health Potion", "type": "health", "amount": 250, "price": 100},
    {"name": "Giant Health Potion", "type": "health", "amount": 500, "price": 180},
    {"name": "Ultimate Health Potion", "type": "health", "amount": "full", "price": 300},

    # Mana Potions
    {"name": "Small Mana Potion", "type": "mana", "amount": 30, "price": 25},
    {"name": "Medium Mana Potion", "type": "mana", "amount": 75, "price": 50},
    {"name": "Large Mana Potion", "type": "mana", "amount": 150, "price": 100},
    {"name": "Giant Mana Potion", "type": "mana", "amount": 300, "price": 180},
    {"name": "Ultimate Mana Potion", "type": "mana", "amount": "full", "price": 300},

    # Mixed Potions
    {"name": "Small Mixed Potion", "type": "mixed", "hp": 50, "mana": 30, "price": 60},
    {"name": "Medium Mixed Potion", "type": "mixed", "hp": 100, "mana": 75, "price": 100},
    {"name": "Large Mixed Potion", "type": "mixed", "hp": 200, "mana": 150, "price": 180},

    # Buff Potions
    {"name": "Attack Potion", "type": "attack_buff", "amount": 10, "duration": 3, "price": 150},
    {"name": "Defense Potion", "type": "defense_buff", "amount": 10, "duration": 3, "price": 150}
]

bosses = {

    10: {
        "name": "Goblin King",
        "hp": 300,
        "attack": 30,
        "defense": 12,
        "exp": 500,
        "gold": 250
    },

    20: {
        "name": "Forest Guardian",
        "hp": 500,
        "attack": 45,
        "defense": 20,
        "exp": 800,
        "gold": 400
    },

    30: {
        "name": "Ancient Golem",
        "hp": 700,
        "attack": 60,
        "defense": 30,
        "exp": 1200,
        "gold": 600
    },

    40: {
        "name": "Vampire Lord",
        "hp": 900,
        "attack": 75,
        "defense": 35,
        "exp": 1600,
        "gold": 800
    },

    50: {
        "name": "Dragon Rider",
        "hp": 1200,
        "attack": 90,
        "defense": 45,
        "exp": 2000,
        "gold": 1000
    },

    60: {
        "name": "Demon General",
        "hp": 1500,
        "attack": 110,
        "defense": 55,
        "exp": 2500,
        "gold": 1300
    },

    70: {
        "name": "Ice Titan",
        "hp": 1800,
        "attack": 125,
        "defense": 65,
        "exp": 3000,
        "gold": 1600
    },

    80: {
        "name": "Shadow Emperor",
        "hp": 2200,
        "attack": 145,
        "defense": 75,
        "exp": 3500,
        "gold": 2000
    },

    90: {
        "name": "Celestial Dragon",
        "hp": 2600,
        "attack": 165,
        "defense": 85,
        "exp": 4000,
        "gold": 2500
    },

    100: {
        "name": "Ancient Demon King",
        "hp": 3500,
        "attack": 200,
        "defense": 100,
        "exp": 5000,
        "gold": 5000
    }
}