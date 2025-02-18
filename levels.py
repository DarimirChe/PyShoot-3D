from objects import *

levels = [
    {
        "name": "Коробка",
        "background": "box.png",
        "map": "Box.txt",
        "player_position": (12, 6.5, 0),
        "sky": "Sky",
        "ground": (80, 111, 80),
        "objects": [
            Pin(2, 2, 10, 50, 2, 0.35, speed=2),
            Pin(2, 11, 10, 50, 2, 0.35, speed=2),
            Pin(23, 2, 10, 50, 2, 0.35, speed=2),
            Pin(23, 11, 10, 50, 2, 0.35, speed=2),
            Barrel(7, 5),
            Barrel(7, 8),
            Barrel(17, 5),
            Barrel(17, 8)
        ]
    },
    {
        "name": "Поле",
        "background": "field.png",
        "map": "Field.txt",
        "player_position": (3, 3, 0),
        "sky": "Sky",
        "ground": (193, 146, 0),
        "objects": [
            Barrel(3, 5),
            Barrel(7, 7),
            Devil(2, 11, 20, 100, 2, 0.35, speed=2),
            Devil(8, 2, 20, 100, 2, 0.35, speed=2),
            Devil(17, 5, 20, 100, 2, 0.35, speed=2),
            Devil(22, 2, 20, 100, 2, 0.35, speed=2),
            Devil(24, 11, 20, 100, 2, 0.35, speed=2)
        ]
    },
    {
        "name": "Лесной особняк",
        "background": "mansion.png",
        "map": "Forest_Mansion.txt",
        "player_position": (13, 11, 3 / 4 * math.pi),
        "sky": "Sky",
        "ground": (80, 111, 80),
        "objects": [
            Ghost(2, 2, 15, 100, 1, speed=PLAYER_RUNNING_SPEED),
            Ghost(2, 6, 15, 100, 1, speed=PLAYER_RUNNING_SPEED),
            Ghost(2, 11, 15, 100, 1, speed=PLAYER_RUNNING_SPEED),
            Ghost(24, 2, 15, 100, 1, speed=PLAYER_RUNNING_SPEED),
            Ghost(24, 6, 15, 100, 1, speed=PLAYER_RUNNING_SPEED),
            Ghost(24, 11, 15, 100, 1, speed=PLAYER_RUNNING_SPEED)
        ]
    },
    {
        "name": "Госпиталь",
        "background": "hospital.png",
        "map": "Hospital.txt",
        "player_position": (2, 2, 0),
        "sky": "Sky",
        "ground": (80, 111, 80),
        "objects": [
            Pin(6, 1.5, 20, 50, 2, 0.35, speed=3),
            Pin(4, 11, 20, 50, 2, 0.35, speed=3),
            Pin(10, 11, 20, 50, 2, 0.35, speed=3),
            Devil(4, 5, 30, 100, 2, 0.35, speed=2),
            Devil(11, 10, 30, 100, 2, 0.35, speed=2),
            Devil(22, 6, 30, 100, 2, 0.35, speed=2),
            Ghost(17, 8.5, 15, 50, 1, speed=PLAYER_RUNNING_SPEED),
            Ghost(2, 11, 15, 50, 1, speed=PLAYER_RUNNING_SPEED),
            Ghost(22, 11, 15, 50, 1, speed=PLAYER_RUNNING_SPEED)
        ]
    },
    {
        "name": "Деревня",
        "background": "village.png",
        "map": "Village.txt",
        "player_position": (10, 2.5, 0),
        "sky": "Sky",
        "ground": (80, 111, 80),
        "objects": [
            Pin(2, 11, 20, 100, 2, 0.35, speed=3),
            Pin(15, 2, 20, 100, 2, 0.35, speed=3),
            Pin(20, 6, 20, 100, 2, 0.35, speed=3),
            Pin(24, 2, 20, 100, 2, 0.35, speed=3),
            Pin(5, 7, 20, 100, 2, 0.35, speed=3),
            Devil(10, 3, 30, 200, 2, 0.35, speed=3),
            Devil(8, 3, 30, 200, 2, 0.35, speed=3),
            Devil(2, 6, 30, 200, 2, 0.35, speed=3),
            Devil(2, 8, 30, 200, 2, 0.35, speed=3),
            Devil(15, 10, 30, 200, 2, 0.35, speed=3),
            Devil(19, 3, 30, 200, 2, 0.35, speed=3),
            Ghost(24, 3, 20, 75, 1, speed=PLAYER_RUNNING_SPEED),
            Ghost(21, 8.5, 15, 75, 1, speed=PLAYER_RUNNING_SPEED),
        ]
    }
]
