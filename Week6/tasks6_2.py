# Теперь нужно населить игровой мир различными существами. Ваш гейм-дизайнер придумал сложную разветвленную иерархию существ.

# Во-первых, все существа делятся на земных, морских и воздушных. Среди земных существ выделяются тролли и эльфы, среди морских — русалки и сирены, среди воздушных — драконы и пегасы.

# Создайте базовый класс Creature, а также его наследников:

# ●     EarthCreature (с подклассами Troll и Elf),

# ●     SeaCreature (с подклассами Mermaid и Siren),

# ●     AirCreature (с подклассами Dragon и Pegasus).

class Creature:
    pass

class EarthCreature(Creature):
    health_points: int
    pass


class Troll(EarthCreature):
    health_points: int = 100
    pass


class Elf(EarthCreature):
    health_points: int = 80
    pass


class SeaCreature(Creature):
    health_points: int
    pass


class Mermaid(SeaCreature):
    health_points: int = 60
    pass


class Siren(SeaCreature):
    health_points: int = 75
    pass


class AirCreature(Creature):
    health_points: int
    pass


class Dragon(AirCreature):
    health_points: int = 120
    pass


class Pegasus(AirCreature):
    health_points: int = 85
    pass


x = Elf()
print(isinstance(x, EarthCreature),
isinstance(x, Creature),       
x.health_points, sep='\n')