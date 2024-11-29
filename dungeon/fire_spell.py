from dungeon.creature import Creature
from dungeon.spell import Spell
from dungeon.weapons import MAGIC


class FireSpell(Spell):
    def apply(self, subject: Creature):
        subject.apply_damage(damage=self.amplitude, damage_type=MAGIC)
