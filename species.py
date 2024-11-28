SPECIES = {
  "human": {
    "base_stats": {
      "strength": 1,
      "dexterity": 1,
      "magic": 1,
      "charisma": 1
    }
  },
  "dwarf": {
    "base_stats": {
      "strength": 2,
      "dexterity": 2,
      "magic": 0,
      "charisma": 0
    }
  },
  "elf": {
    "base_stats": {
      "strength": 0,
      "dexterity": 2,
      "magic": 2,
      "charisma": 0
    }
  },
  "halfling": {
    "base_stats": {
      "strength": 0,
      "dexterity": 2,
      "magic": 0,
      "charisma": 2
    }
  }
}


class Species:
    def __init__(self, name: str, base_stats: dict[str, int]):
        self.name = name
        self.base_stats = base_stats


def get_species(name: str) -> Species:
    return Species(name=name, base_stats=SPECIES[name]["base_stats"])
