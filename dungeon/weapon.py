from dungeon.weapons import WEAPONS, MELEE, RANGED, MAGIC


class Weapon:
    def __init__(self, name: str, damage: int, damage_type: str):
        self.name = name
        self.damage = damage
        self.damage_type = damage_type


def get_weapon(name: str) -> Weapon:
    weapon_dict = WEAPONS[name]
    return Weapon(
        name=name,
        damage=weapon_dict["damage"],
        damage_type=weapon_dict["damage_type"]
    )
