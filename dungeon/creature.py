from dungeon.buff import Buff
from dungeon.effect import Effect
from dungeon.spells.spell import Spell
from dungeon.species import Species
from dungeon.stats import STRENGTH, DEXTERITY, MAGIC as MAGIC_STAT
from dungeon.weapons import MELEE, RANGED, MAGIC as MAGIC_DAMAGE_TYPE
from dungeon.weapon import Weapon

import logging


logger = logging.getLogger(__name__)


BASE_MAX_HEALTH = 3
BASE_MAX_MANA = 2
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
        spells: list[Spell] | None = None,
        effects: list[Effect] | None = None,
        health: int | None = None,
        mana: int | None = None,
    ):
        if buffs is None:
            buffs = []
        if spells is None:
            spells = []
        if effects is None:
            effects = []
        self.stats = species.base_stats.copy()
        for buff in buffs:
            self.stats[buff.stat] += 1
        self.name = name
        self.weapon = weapon
        self.buffs = buffs
        self.spells = spells
        self.effects = effects
        self.max_health = BASE_MAX_HEALTH + self.stats[STRENGTH]
        self.max_mana = BASE_MAX_MANA + self.stats[MAGIC_STAT]
        if health is None:
            health = self.max_health
        if mana is None:
            mana = self.max_mana
        self.health = health
        self.mana = mana
        

    def get_damage(self, damage_type: str) -> int:
        damage = self.stats[STATS_BY_DAMAGE_TYPE[damage_type]]
        if self.weapon is not None and self.weapon.damage_type == damage_type:
            damage += self.weapon.damage
        return damage

    def add_effect(self, effect: Effect):
        for pre_existing_effect in self.effects:
            effect = pre_existing_effect.affect(effect)
        self.effects = [e for e in self.effects if e.persist]
        if effect.persist:
            self.effects.append(effect)
        effect.apply(self)

    def is_alive(self):
        return self.health > 0

    def get_spell(self, name: str) -> Spell | None:
        spells = [s for s in self.spells if s.name == name]
        if len(spells) > 0:
            return spells[0]

    def cast(self, spell_name: str) -> Spell:
        spell = self.get_spell(spell_name)
        if spell is None or spell.cost > self.mana:
            raise ValueError(f"{self.name} cannot cast {spell_name}")
        self.mana -= spell.cost
        return spell
