from dungeon.creature import Creature
from dungeon.spells.spell import Spell
from dungeon.effect import MagicDamage


class Fire(Spell):
    def apply(self, subject: Creature):
        damage_effect = MagicDamage(
            amplitude=self.amplitude,
        )
        subject.add_effect(damage_effect)

    def get_difficulty(self):
        return self.amplitude * 4
