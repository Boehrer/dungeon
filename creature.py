from buff import Buff
from spell import Spell
from species import Species
from stats import STRENGTH, DEXTERITY, MAGIC as MAGIC_STAT
from weapons import MELEE, RANGED, MAGIC as MAGIC_DAMAGE_TYPE
from weapon import Weapon


STATS_BY_DAMAGE_TYPE = {
    MELEE: STRENGTH,
    RANGED: DEXTERITY,
    MAGIC_DAMAGE_TYPE: MAGIC_STAT,
}


class Creature:
    def __init__(
        self,
        name: str,
        species: Species,
        weapon: Weapon | None = None,
        buffs: list[Buff] | None = None,
        spells: list[Spell] | None = None
    ):
        if buffs is None:
            buffs = []
        if spells is None:
            spells = []
        self.stats = species.base_stats.copy()
        for buff in buffs:
            self.stats[buff.stat] += 1
        self.name = name
        self.weapon = weapon
        self.buffs = buffs
        self.spells = spells

    def get_damage(self, damage_type: str) -> int:
        damage = self.stats[STATS_BY_DAMAGE_TYPE[damage_type]]
        if self.weapon.damage_type == damage_type and self.weapon is not None:
            damage += self.weapon.damage
        return damage

    def apply_damage(self, damage: int):
        pass
