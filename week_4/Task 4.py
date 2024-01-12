class Creature:
    health_points: int

    def __init__(self):
        self.health_points = 0

class EarthCreature(Creature):
    health_points = 0

class Troll(EarthCreature):
    health_points = 100

class Elf(EarthCreature):
    health_points = 80

class SeaCreature(Creature):
    health_points = 0

class Mermaid(SeaCreature):
    health_points = 60

class Siren(SeaCreature):
    health_points = 75

class AirCreature(Creature):
    health_points = 0

class Dragon(AirCreature):
    health_points = 120

class Pegasus(AirCreature):
    health_points = 85