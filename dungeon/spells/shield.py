from dungeon.creature import Creature
from dungeon.spell.spell import Spell
from dungeon.effect import Shield


class Shield(Spell):
    def apply(self, subject: Creature):
        shield_effect = Shield(
            amplitude=self.amplitude,
            duration=100,
        )
        subject.add_effect(shield_effect)
