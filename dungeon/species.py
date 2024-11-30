class Species:
    def __init__(self, name: str, base_stats: dict[str, int]):
        self.name = name
        self.base_stats = base_stats


human = Species(
    name="human",
    base_stats={"strength": 1, "dexterity": 1, "magic": 1, "charisma": 1},
)
dwarf = Species(
    name="dwarf",
    base_stats={"strength": 2, "dexterity": 2, "magic": 0, "charisma": 0},
)
elf = Species(
    name="elf",
    base_stats={"strength": 0, "dexterity": 2, "magic": 2, "charisma": 0},
)
halfling = Species(
    name="halfling",
    base_stats={"strength": 0, "dexterity": 2, "magic": 0, "charisma": 2},
)
