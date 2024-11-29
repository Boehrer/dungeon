from spell import Spell

from creature import Creature
from weapons import MAGIC


class FireSpell(Spell):
    def apply(self, subject: Creature):
        subject.apply_damage(damage=self.amplitude, damage_type=MAGIC)
