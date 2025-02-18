from objects import *

levels = [
    {
        "name": "Коробка",
        "map": "Box.txt",
        "player_position": (12, 12, 0),
        "sky": "Sky",
        "ground": (80, 111, 80),
        "objects": [
            Barrel(2, 2),
            Barrel(7, 7),
        ]
    },
    {
        "name": "Поле",
        "map": "Field.txt",
        "player_position": (3, 3, 0),
        "sky": "Sky",
        "ground": (193, 146, 0),
        "objects": [
            Barrel(2, 2),
            Barrel(7, 7),
        ]
    },
    {
        "name": "Лесной особняк",
        "map": "Forest_Mansion.txt",
        "player_position": (14, 8, 0),
        "sky": "Sky",
        "ground": (80, 111, 80),
        "objects": [
            Barrel(2, 2),
            Barrel(7, 7),
        ]
    },
    {
        "name": "Госпиталь",
        "map": "Hospital.txt",
        "player_position": (2, 1.5, 0),
        "sky": "Sky",
        "ground": (80, 111, 80),
        "objects": [
            Barrel(2, 2),
            Barrel(7, 7),
        ]
    },
    {
        "name": "Деревня",
        "map": "Village.txt",
        "player_position": (4, 3, 0),
        "sky": "Sky",
        "ground": (80, 111, 80),
        "objects": [
            Barrel(2, 2),
            Barrel(7, 7),
        ]
    }
]
