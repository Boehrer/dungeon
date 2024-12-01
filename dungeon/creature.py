import copy
import logging

from dungeon.effect import Effect
from dungeon.hat import Hat
from dungeon.spells.spell import Spell
from dungeon.species import Species
from dungeon.stats import STRENGTH, DEXTERITY, MAGIC as MAGIC_STAT
from dungeon.weapons import MELEE, RANGED, MAGIC as MAGIC_DAMAGE_TYPE
from dungeon.weapon import Weapon



logger = logging.getLogger(__name__)


BASE_MAX_HEALTH = 3
BASE_MAX_MANA = 2


class Creature:
    def __init__(
        self,
        name: str,
        species: Species,
        weapon: Weapon | None = None,
        hat: Hat | None = None,
        buffs: dict[str, int] | None = None,
        spells: list[Spell] | None = None,
        effects: list[Effect] | None = None,
        health: int | None = None,
        mana: int | None = None,
    ):
        if buffs is None:
            buffs = {}
        if spells is None:
            spells = []
        if effects is None:
            effects = []
        self.stats = species.base_stats.copy()
        for stat, buff in buffs.items():
            self.stats[stat] += buff
        self.name = name
        self.weapon = weapon
        self.hat = hat
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

    def add_effect(self, effect: Effect):
        for pre_existing_effect in self.effects:
            effect = pre_existing_effect.affect(effect)
        self.effects = [e for e in self.effects if e.persist]
        if effect.persist:
            self.effects.append(effect)
        effect.apply(self)

    def is_alive(self):
        return self.health > 0
